from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# Create your models here.

class Irasas(models.Model):
    pavadinimas = models.CharField(max_length=70, null=False)
    tekstas = models.TextField(null=False)
    kategorija = models.CharField(max_length=40, null=False)
    vartotojas = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pavadinimas

    class Meta:
        verbose_name = 'Įrašas'
        verbose_name_plural = 'Įrašai'


# class Profilis(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nuotrauka = models.ImageField(default='default.png', upload_to='profile_pics')
#
#     class Meta:
#         verbose_name = 'Profilis'
#         verbose_name_plural = 'Profiliai'
#     def __str__(self):
#         return f'{self.user.username} profilis'
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         img = Image.open(self.nuotrauka.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300,300)
#             img.thumbnail(output_size)
#             img.save(self.nuotrauka.path)
