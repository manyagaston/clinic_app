from django.urls import path
from agents.views import AgentsListView
from agents.docteurs.views import DocteurCreateView,DocteurListView
from agents.infirmiers.views import InfirmiersCreateView,InfirmiersListView

urlpatterns = [
    # ça nous liste les 3 pages pricipale de notre projet
    path('', AgentsListView.as_view(), name='list_age'),
    # La route docteurs/ permet de lister tout les docteurs du clinic ainsi que leur matricule
    path('docteurs/', DocteurListView.as_view(), name='list_docteur'),
    # la route infirmiers/ nous liste toutes les infirmiers dans une tamble
    path('infirmiers/', InfirmiersListView.as_view(), name='list_infirmier'),
    # la route add_docteur/ nous permet juste d'ajouter les docteurs dans la BD
    path('add_docteur/', DocteurCreateView.as_view(), name='add_docteur'),
    # la route add_infirmier/ permet d'ajouter uniquement les infirmiers dans la BD
    path('add_infirmier/', InfirmiersCreateView.as_view(), name='add_infirmier'),
]