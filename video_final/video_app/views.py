from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import VideoSerializer
from .models import Video

class Upload(viewsets.ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer
