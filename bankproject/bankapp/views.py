from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matched')
            return redirect(request,'register.html')
        return redirect('/')
    return render(request,'register.html')
def contact(request):
    return render(request,'contact.html')