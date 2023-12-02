from django.db import models

from django.contrib.auth.models import User


class Employe(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    jours_de_travail = models.CharField(max_length=255)
    demi_jour_mercredi = models.BooleanField()
    nombre_jours_de_travail = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

