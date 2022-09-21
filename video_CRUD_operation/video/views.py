from django.shortcuts import render,redirect
from .models import Video
from .forms import Video_form
from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
   video=Video.objects.all()
   page = request.GET.get('page',4)
   paginator= Paginator(video,4)
   try:
      users = paginator.page(page)
   except PageNotAnInteger:
        users = paginator.page(1)
   except EmptyPage:
        users = paginator.page(paginator.num_pages)
   return render(request,"index.html",{"users":users})

def ADD(request):
     if request.method =="POST":
          form=Video_form(data=request.POST,files=request.FILES)
          if form.is_valid():
            form.save()
            msg="Video Uplaoded"
            url="/add/?output={}".format(msg)
            #return HttpResponseRedirect(url)
            return redirect('index',)
          return render(request,'add.html',{'form':form})
     else:
          form=Video_form()
     return render(request,'add.html',{'form':form})

     
def EDIT(request,id):
     if request.method =="POST":
          if id==0:
               form=Video_form(data=request.POST,files=request.FILES)

          else:
               vd=Video.objects.get(id=id)
               form=Video_form(data=request.POST,files=request.FILES,instance=vd)
               if form.is_valid():
                    form.save()

               return redirect('index')

     
     elif request.method=="GET":
          if id==0:          
               form=Video_form()
          else:
               vd=Video.objects.get(id=id)
               form=Video_form(instance=vd)
          return render(request,'edit.html',{'form':form})

def DELETE(request,id):
     vd=Video.objects.get(id=id)
     vd.delete()
     return redirect('index')
