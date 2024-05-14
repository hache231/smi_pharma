from django.shortcuts import render

def login_page(request):
    return render(request, 'login.html')

def logout(request):
    pass


