from django import forms
from .models import Irasas
from django.contrib.auth.models import User


class IrasoKurimoForma(forms.ModelForm):
    class Meta:
        model = Irasas
        fields = ['pavadinimas', 'tekstas', 'kategorija']

class IrasoAtnaujinimoForma(forms.ModelForm):
    class Meta:
        model = Irasas
        fields = ['pavadinimas', 'tekstas', 'kategorija']

class ProfilioRedagavimoForma(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# class ProfilisAtnaujinimoForma(forms.ModelForm):
#     class Meta:
#         model = Profilis
#         fields = ['nuotrauka']
