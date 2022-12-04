from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'notes/index.html')

def main(request):
    return render(request, 'notes/main.html')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paskyra sukurta sėkmingai')
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

# def login(request):
#     return render(request, 'registration/login.html')

def profile(request):
    return render(request, 'registration/profile.html')

def logout(request):
    return render(request, 'registration/logout.html')

def update(request):
    return render(request, 'notes/update.html')
