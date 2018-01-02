import os, fnmatch
from os import rename
from glob import glob
class find(object):
	def __init__(self):
		pass
	def find_name(self, pattern, path):
		os.chdir(path)
		for root, sudo, files in os.walk(path):
			for fname in glob('*.mkv'):
				return fname

	def find_link(self, pattern, path):
		os.chdir(path)
		for root, sudo, files in os.walk(path):
			for fname in glob('*.mkv'): 
				rename(fname, fname.replace(" ", ""))
				for fname2 in glob('*.mkv'):
					link = os.path.join(root,fname2)
					return link
	def find_link_(self, pattern, path):
		os.chdir(path)
		for root, sudo, files in os.walk(path):
			for fname in glob('*.mkv'): 
				rename(fname, fname.replace(" ", ""))
				for fname2 in glob('*.mkv'):
					return fname2




