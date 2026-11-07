"""Rebuild approved poses from retained raw sources and verify assembly provenance."""
from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image

R=Path(__file__).resolve().parents[1]
S=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
def module(name,file):
    spec=importlib.util.spec_from_file_location(name,S/file)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
extract=module('extract','extract_strip_frames.py')
assembler=module('assemble','assemble_extended_atlas.py')
manifest=json.loads((R/'frames/frames-manifest.json').read_text())
before=Image.open(R/'qa/atlas-pre-despill.png').convert('RGBA')
final_path=R/'final/spritesheet-extended.webp'
final=Image.open(final_path).convert('RGBA')
records=[]
for row,(state,count) in enumerate(extract.ROW_FRAME_COUNTS.items()):
    record=next(r for r in manifest['rows'] if r['state']==state)
    source=Path(record['source'])
    assert hashlib.sha256(source.read_bytes()).hexdigest()==record['source_sha256']
    strip=extract.remove_chroma_background(Image.open(source),(0,255,0),96)
    if record['method']=='stable-slots':
        frames=extract.extract_stable_slot_frames(strip,count)
    elif record['method']=='reviewed-layout':
        layout_path=R/'qa'/f'{state}-source-layout.json'
        frames,_=extract.extract_reviewed_layout(strip,count,json.loads(layout_path.read_text())[state],layout_path.parent)
    elif record['method']=='components':
        frames=extract.extract_component_frames(strip,count)
    else:
        raise AssertionError(record['method'])
    for col,frame in enumerate(frames):
        saved=Image.open(R/'frames'/state/f'{col:02}.png').convert('RGBA')
        assert frame.tobytes()==saved.tobytes(),(state,col,'source extraction')
        composed=Image.new('RGBA',(192,208))
        composed.alpha_composite(frame)
        box=(col*192,row*208,(col+1)*192,(row+1)*208)
        assert composed.tobytes()==before.crop(box).tobytes(),(state,col,'preclean atlas')
        assert composed.getchannel('A').tobytes()==final.crop(box).getchannel('A').tobytes(),(state,col,'alpha')
    records.append({'state':state,'source':str(source.relative_to(R)),'source_sha256':record['source_sha256'],'method':record['method'],'frame_count':count,'source_frame_mapping':list(range(count)),'exact_source_reconstruction':True})
scale=json.loads((R/'qa/look-row-9-registration.json').read_text())['scale']
neutral=assembler.load_neutral_cell(R/'frames/idle/00.png',before,(0,255,0),96)
look=[]
for row in (9,10):
    source=R/'decoded'/f'look-row-{row}.png'
    frames=assembler.normalize_cells_to_reference(assembler.extract_row_strip_cells(source,(0,255,0),96),neutral,scale)
    for col,frame in enumerate(frames):
        composed=Image.new('RGBA',(192,208))
        composed.alpha_composite(frame)
        composed=assembler.clear_transparent_rgb(composed)
        assert composed.tobytes()==before.crop((col*192,row*208,(col+1)*192,(row+1)*208)).tobytes(),(row,col,'look source reconstruction')
    look.append({'row':row,'source':str(source.relative_to(R)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'frame_count':8,'shared_scale':scale,'exact_source_reconstruction':True})
assert before.getchannel('A').tobytes()==final.getchannel('A').tobytes()
report={'ok':True,'atlas_sha256':hashlib.sha256(final_path.read_bytes()).hexdigest(),'standard_source_frames_verified':sum(r['frame_count'] for r in records),'look_source_frames_verified':16,'whole_atlas_alpha_unchanged_by_single_final_cleanup':True,'rows':records,'look_rows':look,'extractor_sha256':hashlib.sha256((S/'extract_strip_frames.py').read_bytes()).hexdigest(),'assembler_sha256':hashlib.sha256((S/'assemble_extended_atlas.py').read_bytes()).hexdigest()}
(R/'qa/source-reconstruction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('ok','atlas_sha256','standard_source_frames_verified','look_source_frames_verified')}))
