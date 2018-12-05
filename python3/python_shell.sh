#!/usr/bin/python

import os
import subprocess

## Executing command using variable
cmd = 'pwd'
os.system(cmd)

## Executing command
os.system("date")


import commands
commands.getoutput("cal")
commands.getstatusoutput("cal")

#subprocess.run(['ls', '-l'])

#bash.ls("-dl") 

#os.popen("ls -l").read()

