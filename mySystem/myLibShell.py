#!/usr/bin/env python
import os
import glob
import pydoc

## TODO:
# [] Include the py_store in systemPath.
#
def colored_output():
	## TODO:
	## Place this lines where you want
	## to call for colored output.
	my_colors = myLibShell.Bcolors
	print(my_colors.FAIL + "Peligro: 3m..2m.1m:" + my_colors.ENDC)

def list_files():
	ls = glob.glob('*')

	for a_file in ls:
		#print(a_file)
		print(" {0:>2} ".format(a_file))

def print_pwd():
	print(os.getcwd())

def change_dir(path):
	os.chdir(path)

def my_pydoc_pager(text):
	pydoc.pager(text)
	






#os.system(cmd)
#list_files()
#print_pwd()
#change_dir('linux/')
#my_pydoc_pager('text texttexttext texttext\ntext texttexttext texttext ')


