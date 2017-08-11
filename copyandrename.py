import os
from os.path import join
from shutil import copy

name = raw_input('enter the type of files you want to delete\n')
for (dirname, dirs, files) in os.walk('.'):
	for filename in files:
		if filename.endswith(name):
			thefile = os.path.join(dirname, filename)
			dest_dir = ur'./testdir'
			copy(thefile, dest_dir)
			copy_file = os.path.join(dest_dir, filename)
			new_name = os.path.join(dest_dir, filename.replace('.py', ''))
			os.rename(copy_file, new_name)