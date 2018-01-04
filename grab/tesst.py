import os, youtube_dl
from pathlib import Path
from glob import glob
from os import rename

download_directory = '/home/kazirahiv/'

def download(link):
	download_link = link
	generated = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' --output \"%(title)s.%(ext)s\" "+ download_link
	print("generated: ", generated)
	video_name = os.popen("youtube-dl --get-filename --output \"%(title)s.%(ext)s\" "+ link).read().replace(" ", "")

	print("Video Name: ", video_name)
	os.chdir(download_directory)
#	os.system(generated)
	file = (download_directory+video_name).replace(" ", "").replace("\n", "").replace(".webm", ".mp4")
	print("File: ", file)
	Xfile = Path(file)
	print("Xfile: ", Xfile)
	os.chdir(download_directory)
	pattern = video_name[:20]+"*"
	#pattern = video_name.replace(".*", "")
	print("Pattern: ", pattern)
	for name in glob(pattern):
			rename(name, name.replace(" ", ""))
	if Xfile.is_file():
		print( "True")