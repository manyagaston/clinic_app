"""
URL configuration for clinic_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # admin/ nous permet d'acceder a la page admin de notre projet 
    path('admin/', admin.site.urls),
    # / inclu les routes qui se trouve dans urls.py de  l'application agents
    path('', include('agents.urls')),
    # malades/ inclu les routes que se trouve dans urls.py de l'application malade
    path('malades/', include('malade.urls')),
]
