#!/usr/bin/env python

import os
import glob



def list_files(path=os.getcwd()):
	
	os.system('clear')
	print path
	print('type a valid path\n \
	\texample: /path/to/directory/\n \
	\tsource tree(st) - build - source - linuxInclude(lxi)\n \
	\tPython local system scripts(pymods)')
	
	path = raw_input()
	
	if (path == 'build'):
		build = '/home/raul/rpmbuild/BUILD/'
		path = build
	if (path == 'source'):
		source = '/home/raul/rpmbuild/SOURCES/'
		path = source
	if (path == 'lxi'):
		linuxInclude = '/home/raul/rpmbuild/BUILD/kernel-3.10.0-1160.118.1.el7/linux-3.10.0-1160.118.1.el7.x86_64/include/linux/'
		path = linuxInclude
	if (path == 'st'):
		sourceTree = '/usr/src/'
		path = sourceTree
	if (path == 'pymods'):
		sourceTree = '/home/raul/Documents/Python2.7/mySystem'
		path = sourceTree
	if (path == ''):
		path = path
	
		
	os.chdir(path)	
	ls = glob.glob('*')

	for a_file in ls:
		#print(a_file)
		print(" {0:>2} ".format(a_file))
		
		

## Implicit call when first loaded the module.
#list_files()
