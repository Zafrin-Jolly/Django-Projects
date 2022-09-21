import code
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import *
from .models import *

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('netflix_app:profile-list')
        return render(request, 'index.html')

method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()

        data = {
            'profiles':profiles
        }
        return render(request, 'profileList.html', data)

class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        data = {
            'form':form
        }
        return render(request, 'profileCreate.html', data)

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('netflix_app:profile-list')
        data = {
            'form':form
        }
        return render(request, 'profileCreate.html', data)

method_decorator(login_required, name='dispatch')
class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            if profile not in request.user.profiles.all():
                return redirect('netflix_app:profile-list')

            data = {
            'movies':movies
            }

            return render(request, 'movieList.html', data)
        except Profile.DoesNotExist:
            return redirect('netflix_app:profile-list')

method_decorator(login_required, name='dispatch')
class MovieDetail(View):
    def get(self, request, movie_code, *args, **kwargs):
        try:
            movies = Movie.objects.get(video_code=movie_code)
            vid=Video.objects.filter(code=movie_code)
            page = request.GET.get('page', 3)
            paginator = Paginator(vid, 4)
            try:
                video = paginator.page(page)
            except PageNotAnInteger:
                video = paginator.page(1)
            except EmptyPage:
                video = paginator.page(paginator.num_pages)
            
            data = {
                'movie':movies,
                'video_list' :video
            }
            return render(request, 'movieDetail.html', data)
        except Movie.DoesNotExist:
            return redirect('netflix_app:movie-list')


method_decorator(login_required, name='dispatch')
class PlayMovie(View):
    def get(self, request, code, *args, **kwargs):
        try:
            video = Video.objects.filter(id=code)
            #movie = movie.video.values()
            
            data = {
                'movie':video
            }

            return render(request, 'index2.html', data)
        except Movie.DoesNotExist:
            return redirect('movie-list')


def search(request):
    movies=Movie.objects.all()
    if request.method=="GET":
        name=request.GET.get('name')
        if name!=None:
            movies=Movie.objects.filter(name__icontains=name)
    

    data={
        'movie':movies
    }
    return render(request,"search.html",data)