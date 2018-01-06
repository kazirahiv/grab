import re
import youtube_dl
import os
from glob import glob
from os import rename
from pathlib import Path
from django.shortcuts import render
from  .models import Download
from django.template import loader
from django.conf import settings
from django.http import HttpResponse 
import time
# Create your views here.
# path to the download dir
download_directory = '/home/kazirahiv/'

def index(request):
	latest_downloads = Download.objects.order_by('dw_date')[:5]
	output = ','.join([q.download_text for q in latest_downloads])
	file = "None"
	downloaded = "None"
	fname = "None"
	if request.method == "POST": 
		link = request.POST.get('link')
		if request.POST.get('checked'):
			b_generated = "youtube-dl --extract-audio --audio-format mp3 --output \"%(title)s.%(ext)s\" "+ link.replace("&t*", "")
			generated = re.sub("&t.*", "", b_generated)
			print(generated)
			video_name = os.popen("youtube-dl --get-filename --output \"%(title)s.%(ext)s\" "+ link).read()
			print("video_name", video_name)
			os.chdir(download_directory)
			os.system(generated)
			file = (download_directory+video_name).replace(" ", "").replace("\n", "").replace(".mp4", ".mp3").replace("#", "").replace(".webm", ".mp3")
			print("File: ", file)
			Xfile = Path(file)
			os.chdir(download_directory)
			pattern = video_name[:20]+"*"
			print(pattern)
			time.sleep(4)
			for name in glob(pattern):
				re.sub(r'[^\w]', ' ', name)
				rename(name, name.replace(" ", "").replace("#", ""))
			if os.path.exists(file):
				downloaded = True
				fname = video_name.replace(" ", "").replace("#", "").replace(".mp4", ".mp3").replace(".webm", ".mp3")
		else:
			generated = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' --output \"%(title)s.%(ext)s\" "+ link
			video_name = os.popen("youtube-dl --get-filename --output \"%(title)s.%(ext)s\" "+ link).read()
			os.chdir(download_directory)
			os.system(generated)
			file = (download_directory+video_name).replace(" ", "").replace("\n", "").replace(".webm", ".mp4").replace("#", "")
			print("File: ", file)
			Xfile = Path(file)
			os.chdir(download_directory)
			pattern = video_name[:30]+"*"
			print(pattern)
			for name in glob(pattern):
				re.sub(r'[^\w]', ' ', name)
				rename(name, name.replace(" ", "").replace("#", ""))
			if os.path.exists(file):
				downloaded = True
				fname = video_name.replace(" ", "").replace("#", "").replace(".webm", ".mp4")
	else:
		downloaded = False
	template = loader.get_template('grab/index.html')
	contex = {'latest_downloads': latest_downloads, 'downloaded':downloaded, 'fname':fname}
	return HttpResponse(template.render(contex, request))




def download(request, file_name):
    file_path = os.path.join(download_directory, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404
