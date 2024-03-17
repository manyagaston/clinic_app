from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Malade
from .forms import MaladeForm

class MaladeListView(ListView):
    model = Malade

class MaladeCreateView(CreateView):
    model = Malade
    form_class = MaladeForm
    success_url = '/malades/'