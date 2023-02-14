from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Etudiant(models.Model):
    matricule = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    nationalite = models.CharField(max_length=30)
    moyenne =  models.CharField(max_length=5)
      
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    # Soft deleting
    archive = models.BooleanField(default=False)
   
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Matiere(models.Model):
    nomMatiere = models.CharField(max_length=200)
    volumeHoraire = models.IntegerField()
    nbCredit = models.IntegerField()
    class Meta:
        db_table="matiere"

class Evaluation(models.Model):
    nomEvaluation = models.CharField(max_length=200)
    typeEvaluation = models.CharField(max_length=200)
    DateEvaluation = models.CharField(max_length=200)
    class Meta:
        db_table="evaluation"

class Semestre(models.Model):
    nomSemestre = models.CharField(max_length=200)
    class Meta:
        db_table="semestre"