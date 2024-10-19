from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Apartament(models.Model):
    numar = models.CharField(max_length=10)
    scara = models.CharField(max_length=10)
    etaj = models.IntegerField()

    def __str__(self):
        return f"Apartament {self.numar}, Scara {self.scara}"


class Locatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    apartament = models.ForeignKey(Apartament, on_delete=models.SET_NULL, null=True)
    telefon = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"Locatar: {self.user.username} - Ap: {self.apartament.numar}"


class FacturaIntretinere(models.Model):
    locatar = models.ForeignKey(Locatar, on_delete=models.CASCADE)
    luna = models.CharField(max_length=20)
    valoare = models.DecimalField(max_digits=7, decimal_places=2)
    achitata = models.BooleanField(default=False)

    def __str__(self):
        return f"Factura: {self.luna} - {self.valoare} lei"


class Avizier(models.Model):
    titlu = models.CharField(max_length=100)
    mesaj = models.TextField()
    data_postarii = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titlu
