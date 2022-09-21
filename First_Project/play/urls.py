from nturl2path import url2pathname
from django.urls import path
from.import views
urlpatterns=[path('',views.home,name='home'),
path('add',views.add,name='add')]

