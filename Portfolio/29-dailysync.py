#!/usr/bin/env python3
import subprocess
import os
from  multiprocessing import Pool

src =os.getcwd()+ "/data/prod/"
dirs=next(os.walk(src))[1]
def backing(dirs):
 dest =os.getcwd()+ "/data/prod_backup/"
 subprocess.call(["rsync", "-arq", src+'/'+dirs, dest])
p=Pool(len(dirs))
p.map(backing,dirs)
