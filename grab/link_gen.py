import os, fnmatch
from os import rename
from glob import glob
def find(pattern, path):
	result = []
	os.chdir(path)
	for root, sudo, files in os.walk(path):
		for fname in glob('*.mkv'):
			result.append(fname)
			rename(fname, fname.replace(" ", ""))
			for fname2 in glob('*.mkv'):
				result.append(os.path.join(root,fname2))
	return result