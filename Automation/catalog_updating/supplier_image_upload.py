#!/usr/bin/env python3
import requests
import os

dir="supplier-data/images/"
url = "http://localhost/upload/"

for file in os.listdir(dir):
    if file.endswith('.jpeg'):
        with open(os.path.join(dir,file), 'rb') as image:
            r = requests.post(url, files={'file': image})

