from django.db import models


class Agents(models.Model):
    '''Definition du Model Agents.'''
    nom = models.CharField(max_length = 25, blank=False)
    post_nom = models.CharField(max_length = 30, blank=False)
    prenom = models.CharField(max_length = 30, blank=False)
    sexe = models.CharField(max_length = 8)
    email = models.EmailField(max_length = 100, blank=False, unique=True)
    telephone = models.CharField(max_length = 20, blank=False, unique=True)

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    def __str__(self):
        return self.nom

