#!/usr/bin/env python
import subprocess
import os
l=os.environ.get('PROGRAM_NAME');
k=l+'.txt'
m='./program/output/'+l+'.txt';
n='./program/'+l;
with open( m, "w+") as output:
    subprocess.call(["python", n], stdout=output);
print  'output will be stored in file /mnt/shared/%s' %k
