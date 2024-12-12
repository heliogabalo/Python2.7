#!/usr/bin/env python

import os
import glob



def list_files(path=os.getcwd()):
	
	os.system('clear')
	default =  path
	print('type a valid path\n \
	\texample: /path/to/directory/\n \
	\tsource tree(st) - build - source - linuxInclude(lxi)\n \
	\tPython local system scripts(pymods)')
	
	path = raw_input()
	
	if (path == 'build'):
		build = '/home/raul/rpmbuild/BUILD/'
		path = build
	elif (path == 'source'):
		source = '/home/raul/rpmbuild/SOURCES/'
		path = source
	elif (path == 'lxi'):
		linuxInclude = '/home/raul/rpmbuild/BUILD/kernel-3.10.0-1160.118.1.el7/linux-3.10.0-1160.118.1.el7.x86_64/include/linux/'
		path = linuxInclude
	elif (path == 'st'):
		sourceTree = '/usr/src/'
		path = sourceTree
	elif (path == 'pymods'):
		sourceTree = '/home/raul/Documents/Python2.7/mySystem'
		path = sourceTree
	else :
		path = default
		print('Typed an empty string; exiting ... ' + path)
		
	os.chdir(path)	
	ls = glob.glob('*')

	for a_file in ls:
		#print(a_file)
		print("{:>1} ".format(a_file)), # comma dumps horizontally
		


## Implicit call when first loaded the module.
#dirFinder.list_files()
#dirFinder.list_files('/home/raul/Repos/')
#dirFinder.list_files(path='/home/raul/Repos/')
