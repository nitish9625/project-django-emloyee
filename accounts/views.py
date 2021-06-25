from django.contrib.messages.api import info
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid username and password")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # print(first_name, email, password1)

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password1)
                user.save()
                print('user created')
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, 'password and confirm passowrd not matching')
            return redirect('register')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

