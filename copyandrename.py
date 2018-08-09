import os
from os.path import join
from shutil import copy

#name = raw_input('enter the type of files you want to delete\n')
name = ".jpg"
#name = ".rar"
for (dirname, dirs, files) in os.walk('/Users/zhaohuaiyi/Downloads'):
	for filename in files:
		if filename.endswith(name):
			thefile = os.path.join(dirname, filename)
			#dest_dir = ur'./testdir'
			dest_dir = '/Users/zhaohuaiyi/Pictures/freshbackmac'
			#dest_dir = ur'/Users/zhaohuaiyi/Movies/Game-of-thrones'
			copy(thefile, dest_dir)
			os.remove(thefile)
			#copy_file = os.path.join(dest_dir, filename)
			#new_name = os.path.join(dest_dir, filename.replace('.py', ''))
			#os.rename(copy_file, new_name)