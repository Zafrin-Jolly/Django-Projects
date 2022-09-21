from xml.etree.ElementInclude import include
from django.urls import include
from django.urls import path
#from django.urls import re_path as url 
from rest_framework import routers
from video_app.views import Upload


router = routers.DefaultRouter()
router.register('Click to watch and upload',  Upload ,'video')


urlpatterns = [ 
    path('',include(router.urls)),

]

# from django.contrib import admin
# from django.urls import path
# from video_app.models import Video
# from video_app.views import VideoCreate, VideoList, VideoDetail

# urlpatterns = [ 
#     path('',VideoCreate.as_view()),
#     path('list/',VideoList.as_view()),
#     path('<int:pk>',VideoDetail.as_view())

# ]