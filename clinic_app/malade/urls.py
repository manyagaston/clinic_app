from django.urls import path
from .views import MaladeListView,MaladeCreateView

urlpatterns = [
    # la route / nous liste juste les malades
    path('', MaladeListView.as_view(), name='list'),
    # la route ad_malade nous aides a ajouter les differentes malades dans la BD ainsi que les matricules agents qui prennent soin de lui
    path('add_malade/', MaladeCreateView.as_view(), name='add_malade'),
]