from django.shortcuts import render
from .models import Employe

def index(request):
    employes = Employe.objects.all()
    return render(request, "pointage/employes.html", {"employes": employes})
