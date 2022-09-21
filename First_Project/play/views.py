from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Zafrin'})
def add(request):
    value1= int(request.GET['num1'])
    value2= int(request.GET['num2'])
    result=value1+value2
    return render(request, "result.html",{'result':result})
