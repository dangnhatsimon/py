#!/usr/bin/env python3
from PIL import Image
import os

dir = "supplier-data/images/"

for file in os.listdir(dir):
    if file.endswith('.tiff'):
        full_file=os.path.join(dir,file)
        #if not os.path.isfile(full_file): continue
        #tiff_file, ext = os.path.splitext(full_file)
        jpeg_file = full_file.replace('.tiff', '.jpeg')
        os.rename(full_file, jpeg_file)
        im = Image.open(jpeg_file)
        im = im.resize((600,400))
        im = im.convert("RGB")
        im.save(os.path.join(jpeg_file))