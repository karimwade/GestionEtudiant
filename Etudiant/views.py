from django.shortcuts import render, get_object_or_404,redirect
from .models import (Etudiant, Matiere, Evaluation, Semestre)


#---------------------------------BEGIN PARTIE CRUD ETUDIANT------------------------------------------#
def addEtudiant(request):
    if(request.method == "POST"):  
        etudiant = Etudiant.objects.create(
            user=request.user,
            matricule=request.POST["matricule"],
            nom=request.POST["nom"],
            prenom= request.POST["prenom"],
            classe= request.POST["classe"],
            sexe= request.POST["sexe"],
            nationalite= request.POST["nationalite"],
            moyenne= request.POST["moyenne"],
        )
        etudiant.save()
        return redirect("/etudiants/")
    return render(request, "pages/etudiant/createEtudiant.html")

def listEudiant(request): 
    
    etudiants = Etudiant.objects.all()
    return render(request, "pages/etudiant/etudiants.html", {'etudiants' : etudiants})

def showEtudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    return render(request, "pages/etudiant/show.html", {'etudiant' : etudiant})


def editEtudiant(request, id):
    etudiant  = get_object_or_404(Etudiant, id=id )
    if(request.method == "POST"):
 
        etudiant = Etudiant.objects.filter(id=etudiant.id).update(
            matricule=request.POST["matricule"],
            nom=request.POST["nom"],
            prenom= request.POST["prenom"],
            classe= request.POST["classe"],
            sexe= request.POST["sexe"],
            nationalite= request.POST["nationalite"],
            moyenne= request.POST["moyenne"],
        )
        return redirect("/etudiants/")
    return render(request, "pages/etudiant/editEtudiant.html", {'etudiant':etudiant})



def deleteEtudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if(request.method == "POST"):
        etudiant.delete()
        return redirect("/etudiants/")
    return render(request, 'pages/etudiant/deleteEtudiant.html', {'etudiant' : etudiant})

#--------------------------------------END CRUD ETUDIANT---------------------------------------------#


#---------------------------------BEGIN PARTIE CRUD MATIERE------------------------------------------#

def createMatiere(request):
    if(request.method == "POST"):
        matiere = Matiere.objects.create(
            nomMatiere=request.POST["nomMatiere"],
            volumeHoraire=request.POST["volumeHoraire"],
            nbCredit=request.POST["nbCredit"],

        )
        matiere.save()
        return redirect("/matiere/")
    return render(request, "pages/Matiere/createMatiere.html")

def listeMatiere(request):    
    matiere = Matiere.objects.all()   
    return render(request, "pages/Matiere/matiere.html", {'matiere' : matiere})

# Affiche un matiere spécifique
def showMatiere(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    return render(request, "pages/Matiere/showMat.html", {'matiere' : matiere})



def editMatiere(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    if (request.method == "POST"):
        matiere = Matiere.objects.filter(id=matiere.id).update(
            nomMatiere=request.POST["nomMatiere"],
            volumeHoraire=request.POST["volumeHoraire"],
            nbCredit=request.POST["nbCredit"],
        )
        return redirect("/matiere/")
    return render(request, "pages/Matiere/editMatiere.html", {'matiere': matiere})


def deleteMatiere(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    if(request.method == "POST"):
        matiere.delete()
        return redirect("/matiere/")
    return render(request, 'pages/matiere/deleteMatiere.html', {'matiere' : matiere})

#---------------------------------END PARTIE CRUD MATIERE---------------------------------------------#


#---------------------------------BEGIN PARTIE CRUD EVALUATION----------------------------------------#

def createEvaluation(request):
    if(request.method == "POST"):
        evaluation = Evaluation.objects.create(
            nomEvaluation=request.POST["nomEvaluation"],
            typeEvaluation=request.POST["typeEvaluation"],
            DateEvaluation=request.POST["DateEvaluation"],

        )
        evaluation.save()
        return redirect("evaluation/")
    return render(request, "pages/Evaluation/createEvaluation.html")


def listeEvaluation(request):  
    evaluation = Evaluation.objects.all()   
    return render(request, "pages/Evaluation/evaluation.html", {'evaluation' : evaluation})


def showEvaluation(request, id):
    evaluation = get_object_or_404(Evaluation, id=id)
    return render(request, "pages/Evaluation/showEval.html", {'evaluation' : evaluation})


def editEvalation(request, id):
    evaluation = get_object_or_404(Evaluation, id=id)
    if (request.method == "POST"):
        evaluation = Evaluation.objects.filter(id=evaluation.id).update(
            nomEvaluation=request.POST["nomEvaluation"],
            typeEvaluation=request.POST["typeEvaluation"],
            DateEvaluation=request.POST["DateEvaluation"],
        )
        return redirect("/evaluation/")
    return render(request, "pages/Evaluation/editEvaluation.html", {'evaluation': evaluation})


def deleteEvaluation(request, id):
    evaluation = get_object_or_404(Evaluation, id=id)
    if(request.method == "POST"):
        evaluation.delete()
        return redirect("/evaluation/")
    return render(request, 'pages/Evaluation/deleteEvaluation.html', {'evaluation' : evaluation})

#---------------------------------END PARTIE CRUD EVALUATION------------------------------------------#


#---------------------------------BEGIN PARTIE CRUD SEMESTRE------------------------------------------#

def createSemestre(request):
    if(request.method == "POST"):
        semestre = Semestre.objects.create(
            nomSemestre=request.POST["nomSemestre"],

        )
        semestre.save()
        return redirect("semestre/")
    return render(request, "pages/Semestre/createSemestre.html")


def listeSemestre(request):
    semestre = Semestre.objects.all()  
    return render(request, "pages/Semestre/semestre.html", {'semestre' : semestre})

# Affiche un semestre spécifique
def showSemestre(request, id):
    semestre = get_object_or_404(Semestre, id=id)
    return render(request, "pages/Semestre/showSem.html", {'semestre' : semestre})


def editSemestre(request, id):
    semestre = get_object_or_404(Semestre, id=id)
    if (request.method == "POST"):
        semestre= Semestre.objects.filter(id=semestre.id).update(
            nomSemestre=request.POST["nomSemestre"],
        )
        return redirect("/semestre/")
    return render(request, "pages/Semestre/editSemestre.html", {'semestre': semestre})


def deleteSemestre(request, id):
    semestre = get_object_or_404(Semestre, id=id)
    if(request.method == "POST"):
        semestre.delete()
        return redirect("/semestre/")
    return render(request, 'pages/Semestre/deleteSemestre.html', {'semestre' : semestre})

#---------------------------------END PARTIE CRUD SEMESTRE------------------------------------------#
