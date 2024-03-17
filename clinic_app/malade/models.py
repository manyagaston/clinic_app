from django.db import models
from agents.docteurs.models import Docteur
from agents.infirmiers.models import Infirmiers

# Create your models here.
class Malade(models.Model):
    nom = models.CharField(max_length = 25)
    post_nom = models.CharField(max_length = 30)
    prenom = models.CharField(max_length = 30)
    sexe = models.CharField(max_length = 8)
    docteur = models.OneToOneField(Docteur, unique=True, on_delete=models.CASCADE)
    infirmier = models.OneToOneField(Infirmiers,unique=True, on_delete=models.CASCADE )

    class Meta:

        verbose_name ='Malade'
        verbose_name_plural ='Malades'

    def __str__(self):
        return self.nom
