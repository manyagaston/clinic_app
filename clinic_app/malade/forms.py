from django.forms import ModelForm
from .models import Malade
from django import forms

class MaladeForm(forms.ModelForm):
    

    class Meta:
        model = Malade
        fields = ["nom","post_nom","prenom","sexe","docteur","infirmier",]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'post_nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.TextInput(attrs={'class': 'form-control'}),
            'docteur': forms.Select(attrs={'class': 'form-control'}),
            'infirmier': forms.Select(attrs={'class': 'form-control'}),
           
        }