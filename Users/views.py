from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.


def login_User(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        if user is not None:



                if username != username:
                    messages.error(request, 'username is incorrect')
                elif password != password:
                    messages.error(request, 'password is incorrect')
                else: 
                    login(request, user)
                    messages.success(request, 'you successfully log in')
                    return redirect('homepage')
        else:
                messages.error(request, 'ERRROR')
                return redirect('login')
    context = {}
    return render(request,'users/login_page.html',context)


def logout_user(request):
    logout(request)
    messages.success(request, 'you successfully logged out')
    return redirect('login')
   