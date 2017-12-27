import os
import youtube_dl
from django.shortcuts import render
from  .models import Download
from django.template import loader
# Create your views here.
from django.http import HttpResponse 
def index(request):
	latest_downloads = Download.objects.order_by('dw_date')[:5]
	output = ','.join([q.download_text for q in latest_downloads])
	if request.method == "POST":
		link = request.POST['link']	
		generated = "youtube-dl "+ link
		os.system(generated)
	template = loader.get_template('grab/index.html')
	contex = {'latest_downloads': latest_downloads}
	return HttpResponse(template.render(contex, request))


