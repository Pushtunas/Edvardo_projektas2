from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Irasas
from .forms import IrasoKurimoForma, IrasoAtnaujinimoForma
# Create your views here.

def index(request):
    return render(request, 'notes/index.html')

def main(request):
    irasai = Irasas.objects.all()
    forma = IrasoKurimoForma()
    if request.method == 'POST':
        forma = IrasoKurimoForma(request.POST)
        if forma.is_valid():
            irasas = forma.save(commit=False)
            irasas.vartotojas = request.user
            irasas.save()
            return redirect('main')

    context = {
        'irasai': irasai,
        'forma': forma
    }
    return render(request, 'notes/main.html', context)

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

def update(request, id):
    atnaujinti_irasa = Irasas.objects.get(id=id)
    forma = IrasoAtnaujinimoForma(instance=atnaujinti_irasa)

    if request.method == 'POST':
        forma = IrasoAtnaujinimoForma(request.POST)
        if forma.is_valid():
            atnaujinti_irasa.pavadinimas = forma.cleaned_data['pavadinimas']
            atnaujinti_irasa.tekstas = forma.cleaned_data['tekstas']
            atnaujinti_irasa.kategorija = forma.cleaned_data['kategorija']
            atnaujinti_irasa.save()
            return redirect('main')

    context = {
        'irasas': atnaujinti_irasa,
        'forma': forma
    }
    return render(request, 'notes/update.html', context)

def delete(request, id):
    trinti_irasa = Irasas.objects.get(id=id)
    trinti_irasa.delete()
    return redirect('main')

