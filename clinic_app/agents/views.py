from django.shortcuts import render
from django.views.generic import ListView
from .models import Agents

class AgentsListView(ListView):
    model = Agents
