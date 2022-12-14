from contextlib import redirect_stderr
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
 
def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        #condition for confirming passport
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'unsername Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user added')
            
        else:
            messages.info(request,'password is not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')