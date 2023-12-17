from django.urls import path
from .views import formulaire_employe
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('abc',views.Smart_planning, name='Smart Planning'),
    path('formulaire_employe/', views.formulaire_employe, name='formulaire_employe'),
]





