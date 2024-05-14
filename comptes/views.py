from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/')
        
        user = authenticate(username=username, password=password)
        
        if(user is None):
            messages.error(request, 'Invalid password')
            return redirect('/')
        else:
            login(request, user)
            return redirect('/pharmacy')
    
    return render(request, 'login.html')

def logout(request):
    pass


