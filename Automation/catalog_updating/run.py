#! /usr/bin/env python3

import os
import requests
import json
import locale

txt_dir='supplier-data/descriptions/'
img_dir='supplier-data/images/'

def getcontent(dir,txt):
    with open(os.path.join(dir,txt),'r') as t:
        content=t.readlines()
    name = content[0].strip()
    weight = int(content[1].replace('lbs',''))
    description = content[2].strip()
    keys=["name", "weight", "description"]
    values=[name, weight, description]
    return dict(zip(keys,values))

for txt in os.listdir(txt_dir):
    if txt.endswith('.txt'):
        data = getcontent(txt_dir,txt)
        for img in os.listdir(img_dir):
            if os.path.splitext(txt)[0] == os.path.splitext(img)[0]:
                data['image_name']=img
        response=requests.post('http://localhost/fruits/',data=data)
        if not response.ok:
            raise Exception("GET failed with status code {}".format(response.status_code))
        
