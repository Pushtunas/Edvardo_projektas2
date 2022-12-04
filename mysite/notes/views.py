from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Irasas
from .forms import IrasoKurimoForma, IrasoAtnaujinimoForma, ProfilioRedagavimoForma
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'notes/index.html')

@login_required
def main(request):
    irasai = Irasas.objects.all()
    form = IrasoKurimoForma()
    if request.method == 'POST':
        form = IrasoKurimoForma(request.POST)
        if form.is_valid():
            irasas = form.save(commit=False)
            irasas.vartotojas = request.user
            irasas.save()
            return redirect('main')

    context = {
        'irasai': irasai,
        'form': form
    }
    return render(request, 'notes/main.html', context)

@csrf_protect
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

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfilioRedagavimoForma(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        messages.success(request, 'Vartotojo informacija atnaujinta sėkmingai.')
        return redirect('profile')
    else:
        form = ProfilioRedagavimoForma(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'registration/profile.html', context)

def logout(request):
    return render(request, 'registration/logout.html')

@login_required
def update(request, id):
    atnaujinti_irasa = Irasas.objects.get(id=id)
    form = IrasoAtnaujinimoForma(instance=atnaujinti_irasa)

    if request.method == 'POST':
        form = IrasoAtnaujinimoForma(request.POST)
        if form.is_valid():
            atnaujinti_irasa.pavadinimas = form.cleaned_data['pavadinimas']
            atnaujinti_irasa.tekstas = form.cleaned_data['tekstas']
            atnaujinti_irasa.kategorija = form.cleaned_data['kategorija']
            atnaujinti_irasa.save()
            return redirect('main')

    context = {
        'irasas': atnaujinti_irasa,
        'form': form
    }
    return render(request, 'notes/update.html', context)

@login_required
def delete(request, id):
    trinti_irasa = Irasas.objects.get(id=id)
    trinti_irasa.delete()
    return redirect('main')

def search(request):
    query = request.GET.get('query')
    search_results = Irasas.objects.filter(Q(pavadinimas__icontains=query) | Q(tekstas__icontains=query))
    return render(request, 'notes/search.html', {'irasai': search_results, 'query': query})
