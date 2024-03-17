from django.db import models
from agents.models import Agents

class Infirmiers(Agents):
    matricule = models.CharField(max_length = 30, blank=False, unique=True)
    
    class Meta:
        verbose_name = 'Infirmier'
        verbose_name_plural = 'Infirmiers'
    
    def __str__(self):
        return self.matricule