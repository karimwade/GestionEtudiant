"""GestionDesEtudiants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('etudiants/', views.listEudiant, name="etudiants"),
    path('create', views.addEtudiant, name="createEtudiant"),
    path('edit/<int:id>', views.editEtudiant, name="editEtudiant"),
    path('delete/<int:id>', views.deleteEtudiant, name="deleteEtudiant"),
    path('show/<int:id>', views.showEtudiant, name="show"),
    path('matiere/', views.listeMatiere, name="matiere"),
    path('createMatiere', views.createMatiere, name="createMatiere"),
    path('showMatiere/<int:id>', views.showMatiere, name="showMatiere"),
    path('editMatiere/<int:id>', views.editMatiere, name="editMatiere"),
    path('deleteMatiere/<int:id>', views.deleteMatiere, name="deleteMatiere"),
    path('evaluation/', views.listeEvaluation, name="evaluation"),
    path('createEvaluation', views.createEvaluation, name="createEvaluation"),
    path('showEval/<int:id>', views.showEvaluation, name="showEvaluation"),
    path('editEval/<int:id>', views.editEvalation, name="editEvaluation"),
    path('deleteEval/<int:id>', views.deleteEvaluation, name="deleteEvaluation"),
    path('semestre/', views.listeSemestre, name="semestre"),
    path('createSemestre', views.createSemestre, name="createSemestre"),
    path('showSemestre/<int:id>', views.showSemestre, name="showSemestre"),
    path('editSem/<int:id>', views.editSemestre, name="editSemestre"),
    path('deleteSemestre/<int:id>', views.deleteSemestre, name="deleteSemestre"),
]
