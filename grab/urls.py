from django.urls import path, include, re_path
from . import views
app_name = 'grab'
urlpatterns= [
	path('', views.index, name='index'),
	re_path('(?P<file_name>.+)/$', views.download, name='download'),
	path('grabStore/', views.grabStore, name='grabStore'),	
	re_path('grabStore/([A-Za-z0-9_\-]{11})/$', views.grabStoreDownload, name='grabStoreDownload'),
	re_path('grabStore/([A-Za-z0-9_\-]{11})/(?P<file_name>.+)/$', views.download, name='download'),
]
