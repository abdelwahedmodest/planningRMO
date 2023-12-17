from django.shortcuts import render, redirect
from .models import Employe
from .forms import EmployeForm


def index(request):
    return render(request,"index.html")

def Smart_planning(request):
    employes = Employe.objects.all()
    return render(request, "pointage/employes.html", {"employes": employes})





def formulaire_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()  # Cela enregistre les données dans la base de données
            return redirect('index')  # Redirige vers une page de confirmation ou une autre vue
    else:
        form = EmployeForm()

    return render(request, 'pointage/formulaire.html', {'form': form})
