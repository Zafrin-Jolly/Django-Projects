from pickle import TRUE
from re import T
from django.db import models

# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100,blank=False,null=True )
    video=models.FileField(upload_to="video/%y",blank=False,null=True)
    thumb=models.FileField(upload_to="thumb/%y",blank=False,null=True)
    def __str__(self):
        return self.caption