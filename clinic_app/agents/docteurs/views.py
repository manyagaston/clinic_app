from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Docteur

class DocteurListView(ListView):
    model = Docteur
    
class DocteurCreateView(CreateView):
    model = Docteur
    fields = ["matricule","nom","post_nom","prenom","sexe","email","telephone",]
    success_url = '/docteurs/'