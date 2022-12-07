from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Irasas(models.Model):
    pavadinimas = models.CharField(max_length=70, null=False)
    tekstas = models.TextField(null=False)
    kategorija = models.CharField(max_length=40, null=False)
    vartotojas = models.ForeignKey(User, on_delete=models.CASCADE)

    sukurta = models.DateTimeField(auto_now_add=True)
    atnaujinta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pavadinimas

    class Meta:
        verbose_name = 'Įrašas'
        verbose_name_plural = 'Įrašai'
