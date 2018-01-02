from django.urls import path, include, re_path
from . import views
app_name = 'grab'
urlpatterns= [
	path('', views.index, name='index'),
	re_path('(?P<file_name>.+)/$', views.download, name='download'),
	
]
