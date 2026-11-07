"""Arrange extracted native-size evidence; creates no new sprite art."""
from pathlib import Path
from PIL import Image
RUN=Path(__file__).resolve().parents[1]
states=['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
images=[Image.open(RUN/f'qa/rows/{state}/native.png').convert('RGB') for state in states if (RUN/f'qa/rows/{state}/native.png').exists()]
sheet=Image.new('RGB',(max(image.width for image in images),sum(image.height for image in images)),'#252d38')
y=0
for image in images:
    sheet.paste(image,(0,y)); y+=image.height
sheet.save(RUN/'qa/standard-progress.png')
