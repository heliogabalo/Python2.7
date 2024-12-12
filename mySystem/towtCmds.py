import os, sys, subprocess, tempfile

page = True
if page:
	path = tempfile.mkstemp()[1]
	tmp_file = open(path, 'a')
	sys.stdout = tmp_file
print '...some text...'
if page:
	tmp_file.flush()
	tmp_file.close()
	p = subprocess.Popen(['less', path], stdin=subprocess.PIPE)
	p.communicate(()
	sys.stdout = sys.__stdout__
