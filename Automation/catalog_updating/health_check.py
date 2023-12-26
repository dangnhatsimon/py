#!/usr/bin/env python3

import shutil, psutil
import os
import emails
import socket

sender ='automation@example.com'
receiver  ="{}@example.com".format(os.environ.get('USER'))
body='Please check your system and resolve the issue as soon as possible.'

du=shutil.disk_usage('/')
error_usage=80
error_disk_space=20
error_free_memory=500
error_hostname='127.0.0.1'

if psutil.cpu_percent(60)>error_usage:
    subject= 'Error - CPU usage is over 80%'
    message=emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)

if (du.free/du.total)*100 <error_disk_space:
    subject= 'Error - Available disk space is less than 20%'
    message=emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)

if du.free<(error_free_memory*1024*1024):
    subject= 'Error - Available memory is less than 500MB'
    message=emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)
    
if socket.gethostbyname(socket.gethostname()) != error_hostname:
    subject= 'Error - localhost cannot be resolved to 127.0.0.1'
    message=emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)