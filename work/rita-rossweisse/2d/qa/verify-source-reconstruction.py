"""Reconstruct all selected source frames and bind them to the cleaned atlas."""
from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image

RUN=Path(__file__).resolve().parents[1]
SKILL=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
def load_module(name,filename):
    spec=importlib.util.spec_from_file_location(name,SKILL/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
extract=load_module('extract','extract_strip_frames.py')
assembler=load_module('assemble','assemble_extended_atlas.py')
manifest=json.loads((RUN/'frames/frames-manifest.json').read_text())
before=Image.open(RUN/'qa/atlas-pre-despill.png').convert('RGBA')
final_path=RUN/'final/spritesheet-extended.webp'
final=Image.open(final_path).convert('RGBA')
records=[]
for row,(state,count) in enumerate(extract.ROW_FRAME_COUNTS.items()):
    record=next(item for item in manifest['rows'] if item['state']==state)
    source=Path(record['source'])
    assert hashlib.sha256(source.read_bytes()).hexdigest()==record['source_sha256']
    strip=extract.remove_chroma_background(Image.open(source),(0,255,0),96)
    if record['method']=='stable-slots':
        frames=extract.extract_stable_slot_frames(strip,count)
    elif record['method']=='reviewed-layout':
        path=RUN/f'qa/{state}-source-layout.json'
        frames,_=extract.extract_reviewed_layout(strip,count,json.loads(path.read_text())[state],path.parent)
    elif record['method'] in ('reviewed-jump-arc','reviewed-gait-viewport'):
        registration=json.loads((RUN/f'qa/{state}-registration.json').read_text())
        assert registration['source_sha256']==record['source_sha256']
        assert registration['source_frame_mapping']==list(range(count))
        frames=[]
        for transform in registration['transforms']:
            sprite=strip.crop(transform['source_box'])
            scale=registration['shared_scale']
            assert transform['destination_size']==[round(sprite.width*scale),round(sprite.height*scale)]
            cell=Image.new('RGBA',(192,208))
            cell.alpha_composite(sprite.resize(tuple(transform['destination_size']),Image.Resampling.LANCZOS),tuple(transform['destination_xy']))
            frames.append(cell)
    elif record['method']=='components':
        frames=extract.extract_component_frames(strip,count)
    else:
        raise AssertionError(record['method'])
    for col,frame in enumerate(frames):
        saved=Image.open(RUN/f'frames/{state}/{col:02d}.png').convert('RGBA')
        assert frame.tobytes()==saved.tobytes(),(state,col,'source extraction')
        composed=Image.new('RGBA',(192,208))
        composed.alpha_composite(frame)
        box=(col*192,row*208,(col+1)*192,(row+1)*208)
        assert composed.tobytes()==before.crop(box).tobytes(),(state,col,'preclean composition')
        assert composed.getchannel('A').tobytes()==final.crop(box).getchannel('A').tobytes(),(state,col,'alpha preservation')
    records.append({'state':state,'source':str(source.relative_to(RUN)), 'source_sha256':record['source_sha256'],
        'method':record['method'],'frame_count':count,'source_frame_mapping':list(range(count)),'exact_source_reconstruction':True})
scale=json.loads((RUN/'qa/look-row-9-registration.json').read_text())['scale']
neutral=assembler.base_neutral_cell(before)
look=[]
for row in (9,10):
    source=RUN/f'decoded/look-row-{row}.png'
    frames=assembler.normalize_cells_to_reference(assembler.extract_row_strip_cells(source,(0,255,0),96),neutral,scale)
    for col,frame in enumerate(frames):
        composed=Image.new('RGBA',(192,208))
        composed.alpha_composite(frame)
        composed=assembler.clear_transparent_rgb(composed)
        box=(col*192,row*208,(col+1)*192,(row+1)*208)
        assert composed.tobytes()==before.crop(box).tobytes(),(row,col,'look source reconstruction')
    look.append({'row':row,'source':str(source.relative_to(RUN)), 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'frame_count':8,'shared_scale':scale,'exact_source_reconstruction':True})
assert before.getchannel('A').tobytes()==final.getchannel('A').tobytes()
report={'ok':True,'atlas_sha256':hashlib.sha256(final_path.read_bytes()).hexdigest(),
    'standard_source_frames_verified':sum(item['frame_count'] for item in records),'look_source_frames_verified':16,
    'whole_atlas_alpha_unchanged_by_single_final_cleanup':True,'rows':records,'look_rows':look,
    'extractor_sha256':hashlib.sha256((SKILL/'extract_strip_frames.py').read_bytes()).hexdigest(),
    'assembler_sha256':hashlib.sha256((SKILL/'assemble_extended_atlas.py').read_bytes()).hexdigest()}
(RUN/'qa/source-reconstruction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({key:report[key] for key in ('ok','atlas_sha256','standard_source_frames_verified','look_source_frames_verified')}))
