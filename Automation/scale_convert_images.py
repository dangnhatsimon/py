'''
Download file from 
'curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie'
and unzip with 'unzip images.zip'
'''
#!/usr/bin/env python3
from PIL import Image
import os

in_dir = "images/"
out_dir = "/opt/icons/"

#The for loop to correct the badly formatted images.
for filename in os.listdir(in_dir):
    if filename != ".DS_Store": #It has a file store from iOS need to be passed
        im = Image.open(os.path.join(in_dir, filename))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(out_dir, filename+".jpeg"))

