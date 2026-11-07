"""Native registered direction strip and adjacent geometry for parent review."""
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

RUN = Path(__file__).resolve().parents[1]
row = Image.open(RUN/'qa/look-row-9-registered.png').convert('RGBA')
assert row.size == (1536,208)
sheet = Image.new('RGB',(1728,240),'#242b34')
draw = ImageDraw.Draw(sheet)
labels = ['000 UP','022.5 UP-RIGHT','045 UP-RIGHT','067.5 UP-RIGHT','090 RIGHT',
          '112.5 DOWN-RIGHT','135 DOWN-RIGHT','157.5 DOWN-RIGHT']
geometry = []
for index,label in enumerate(labels):
    frame = row.crop((192*index,0,192*(index+1),208))
    sheet.paste(frame,(192*index,28),frame)
    draw.text((192*index+5,8),label,fill='white')
    mask = np.array(frame.getchannel('A'))>16
    yy,xx = np.nonzero(mask)
    geometry.append({'degree':label.split()[0],'bbox':list(frame.getchannel('A').getbbox()),
                     'center':[float(xx.mean()),float(yy.mean())],'area':int(mask.sum())})
neutral = Image.open(RUN/'frames/idle/00.png').convert('RGBA')
sheet.paste(neutral,(1536,28),neutral)
draw.text((1541,8),'APPROVED NEUTRAL',fill='#ffe28b')
sheet.save(RUN/'qa/look-row-9-native.png')
record = {'source_sha256':hashlib.sha256((RUN/'decoded/look-row-9.png').read_bytes()).hexdigest(),
          'registered_sha256':hashlib.sha256((RUN/'qa/look-row-9-registered.png').read_bytes()).hexdigest(),
          'geometry':geometry,'purpose':'Geometry is review evidence, never automatic semantic acceptance.'}
(RUN/'qa/look-row-9-geometry.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
