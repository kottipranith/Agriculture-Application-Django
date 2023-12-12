from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'insem.html')
@login_required(login_url="/insem")
def page1(request):
    return render(request,'page1.html')

@login_required(login_url="/insem")
def page2(request):
    return render(request,'page2.html')

def login(request):
    user=auth.authenticate(username='pranith03',password='123456789')
    auth.login(request,user)
    return HttpResponse('You are logged in')

def logout(request):
    auth.logout(request)
    return HttpResponse('You are logged out')