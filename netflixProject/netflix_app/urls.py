from django.urls import path
from .views import *
from . import views

app_name='netflix_app'
urlpatterns = [
    
    path("",Home.as_view(),name="Home"),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<int:movie_code>/', MovieDetail.as_view(), name="movie-detail"),
    path('watch/play/<int:code>/', PlayMovie.as_view(), name="play-movie"),
    path('/search',views.search, name="search"),
]