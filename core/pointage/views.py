from django.shortcuts import render
from .models import Employe

def index(request):
    employes = Employe.objects.all()
    return render(request, "employes.html", {"employes": employes})
