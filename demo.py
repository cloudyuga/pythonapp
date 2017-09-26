#!/usr/bin/env python
import subprocess
import os
l=os.environ.get('PROG');
print l;
m='./program/output/'+l+'.txt';
n='./program/'+l+'.py';
with open( m, "w+") as output:
    subprocess.call(["python", n], stdout=output);

