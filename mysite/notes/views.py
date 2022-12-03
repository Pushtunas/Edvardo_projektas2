from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'notes/index.html')

def main(request):
    return render(request, 'notes/main.html')

def register(request):
    return render(request, 'registration/register.html')

def login(request):
    return render(request, 'registration/login.html')

def profile(request):
    return render(request, 'registration/profile.html')

def logout(request):
    return render(request, 'registration/logout.html')

def update(request):
    return render(request, 'notes/update.html')
