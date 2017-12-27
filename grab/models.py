import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Download(models.Model):
	download_link = models.CharField(max_length=200)
	choice = models.IntegerField(default=1)
	dw_date = models.DateTimeField('downloaded on')
	def __str__(self):
		return self.download_link
	def was_downloaded_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


