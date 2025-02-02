#!/usr/bin/env python


import readline
import rlcompleter
import sys
import os


# The tab completion mechanism call.
readline.parse_and_bind("tab: complete")

# This defines a context to working with, and a custom
# init file_name, so you can have every config specific 
# 'python init' file for each task, independently.
# Call the snippet with the system class of os module.
## 	example: os.system(cmd)
#myPath = '/home/raul/rpmbuild/BUILD/kernel-3.10.0-1160.118.1.el7/linux-3.10.0-1160.118.1.el7.x86_64'
myPath = '/home/raul/Repos/ckb-next-master'

# Working with source:
sys.path.insert(0, '/home/raul/Documents/Python2.7/mySystem/')
#sys.path.insert(1, os.getcwd())

# Kernel specific path. The working directory
#os.chdir(os.path.join(myPath + '/scripts/gdb'))

# User/application working directory
#os.chdir(os.path.join(myPath + ''))

#print()

# Automated starter for a global/general script
cmd = 'python -B /home/raul/Documents/Python2.7/mySystem/.snippets.py -v'

