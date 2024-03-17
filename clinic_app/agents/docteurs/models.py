from django.db import models
from agents.models import Agents

class Docteur(Agents):
    matricule = models.CharField(max_length = 30, blank=False, unique=True)
    
    class Meta:
        verbose_name = 'Docteur'
        verbose_name_plural = 'Docteurs'
    
    def __str__(self):
        return self.matricule