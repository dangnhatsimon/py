#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

txt_dir='supplier-data/descriptions'

def getformat(dir,txt):
    with open(os.path.join(dir,txt),'r') as t:
        content=t.read().strip().splitlines()
    name='name: {}'.format(content[0])
    weight='weight: {}'.format(content[1])
    return '{}<br/>{}<br/><br/>'.format(name, weight)

if __name__ == "__main__":
    report='/tmp/processed.pdf'
    today=date.today().strftime('%B %d, %Y')
    title='Processed Update on {}'.format(today)
    paragraph=''
    for txt in os.listdir(txt_dir):
        if txt.endswith('.txt'):
            paragraph += getformat(txt_dir,txt)
    reports.generate_report(report , title, paragraph)
    
    sender ='automation@example.com'
    receiver  ='{}@example.com'.format(os.environ.get('USER'))
    subject='Upload Completed - Online Fruit Store'
    body='Online Fruit Store Catalog'
    
    message=emails.generate_email(sender,receiver,subject,body,report)
    emails.send_email(message)
    
    