import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    pub_date = models.DateTimeField(auto_now_add=True)
    video_url = "404" #서버에서 URL로 보관하여 시청 페이지에서 볼 것
    uploader = models.CharField(max_length=200)
    views = 0

    def __str__(self):
        return str(self.videofile)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)