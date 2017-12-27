from django.urls import path, include
from . import views
app_name = 'grab'
urlpatterns= [
	path('', views.index, name='index'),
]
