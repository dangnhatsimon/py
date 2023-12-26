#! /usr/bin/env python3

import os
import requests

dir='/data/feedback/'

def txt_feedback(directory):
 list_feedback=[]
 for file in os.listdir(directory):
  if file.endswith('.txt'):
   list_feedback.append(file)
 return list_feedback

def contents(file):
 with open(file,'r') as f:
  reader=f.readlines()
 return {'title': reader[0].strip(),'name':reader[1].strip(),'date':reader[2].strip(),'feedback':reader[3].strip()}

list_txt_feedback=txt_feedback(dir)
for txt in list_txt_feedback:
 data=contents(os.path.join(dir,txt))
 response=requests.post('http://35.237.50.189/feedback/',data=data)
 if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))