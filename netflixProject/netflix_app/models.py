from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('All', 'All'),
    ('adult', 'ADULT'),
    ('Kids', 'Kids'),
)

MOVIE_CHOICES = (
    ('series', 'SERIES'),
    ('single', 'Single'),
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile',blank=True) #can have multiple profile

class Profile(models.Model):
    name=models.CharField(max_length=500)
    age_limit= models.CharField(choices=AGE_CHOICES, max_length=10)
    uuid=models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=1000)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')
    thumbnail = models.ImageField(upload_to='thumbnail')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)
    video_code=models.IntegerField(unique=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')
    code=models.IntegerField()
    thumbnail = models.ImageField(upload_to='thumbnail')

    def __str__(self):
        return self.title
