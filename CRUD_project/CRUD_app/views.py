from django.shortcuts import render,redirect
from .models import Employees
# Create your views here.
def index(request):
    emp= Employees.objects.all()
    return render(request,'index.html',{'emp':emp})
def ADD(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        emp=Employees(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('index')
    return render(request,'index.html')

def EDIT(request):
    emp= Employees.objects.all()
    return render(request,'index.html',{'emp':emp})

def UPDATE(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        emp=Employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('index')
    return redirect(request,'index.html')


def DELETE(request,id):
    emp= Employees.objects.filter(id = id)
    emp.delete()
    return redirect('index')
