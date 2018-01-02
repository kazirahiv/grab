import os
import youtube_dl
from django.shortcuts import render
from  .models import Download
from django.template import loader
from grab.link_gen import find
from django.conf import settings
from django.http import HttpResponse 
# Create your views here.

def index(request):
	X = find()
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
			downloaded_file_name = X.find_name('*.mkv', '/home/kazirahiv/yao')
			file_download_link= X.find_link_('*.mkv', '/home/kazirahiv/yao') 

	else:
		downloaded = False
	template = loader.get_template('grab/index.html')
	contex = {'latest_downloads': latest_downloads, 'downloaded':downloaded, 'file_download_link':file_download_link}
	return HttpResponse(template.render(contex, request))



# path to the upload dir
UPLOAD_DIR = '/home/kazirahiv/yao'


def download(request, file_name):
    file_path = os.path.join(UPLOAD_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404
