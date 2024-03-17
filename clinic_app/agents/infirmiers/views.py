from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Infirmiers

class InfirmiersListView(ListView):
    model = Infirmiers
    
class InfirmiersCreateView(CreateView):
    model = Infirmiers
    fields = ["matricule","nom","post_nom","prenom","sexe","email","telephone",]
    success_url = '/infirmiers/'