import os
import youtube_dl
from django.shortcuts import render
from  .models import Download
from django.template import loader
from grab.link_gen import find
# Create your views here.
from django.http import HttpResponse 
def index(request):
	latest_downloads = Download.objects.order_by('dw_date')[:5]
	output = ','.join([q.download_text for q in latest_downloads])
	downloaded_file_name = "None" 
	file_download_link = "None"
	if request.method == "POST":
		link = request.POST['link']	
		generated = "youtube-dl "+ link
		os.system(generated)
		downloaded = True
		if downloaded:
			temp = find('*.mkv', '/home/kazirahiv/yao')
		downloaded_file_name = temp[0]
		file_download_link =  temp[1]
	else:
		downloaded = False
	template = loader.get_template('grab/index.html')
	contex = {'latest_downloads': latest_downloads, 'downloaded':downloaded, 'file_download_link':file_download_link}
	return HttpResponse(template.render(contex, request))


