from django.db import models

# Create your models here.
class Video(models.Model):
    Title = models.CharField(max_length=100)
    video = models.FileField(upload_to='media/videos/dd.mp4')


    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

