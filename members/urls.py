from django.urls import path
from .import views # imports members/views.py

urlpatterns = [
    path('', views.index, name='index'),
]
