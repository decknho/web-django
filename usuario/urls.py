from django.urls import path
from . import views

urlpatterns = [
    path('logar/', views.logar, name='logar')
]
