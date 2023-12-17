# forms.py
from django import forms
from .models import Employe


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'email', 'jours_de_travail','nombre_jours_de_travail','demi_jour_mercredi']

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'custom-css-class1'}),
            'prenom': forms.TextInput(attrs={'class': 'custom-css-class2'}),
            'email': forms.EmailInput(attrs={'class': 'custom-css-class3'}),
            'jours_de_travail': forms.TextInput(attrs={'class': 'custom-css-class4'}),
            'demi_jour_mercredi': forms.CheckboxInput(attrs={'class': 'custom-css-class5'}),
            'nombre_jours_de_travail': forms.NumberInput(attrs={'class': 'custom-css-class6'}),
        }

#class EmployeForm(forms.ModelForm):
#    class Meta:
#        model = Employe
#        fields = '__all__'  # Utilisez '__all__' pour inclure tous les champs du modèle dans le formulaire
