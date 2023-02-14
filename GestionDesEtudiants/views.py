from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")

def admin(request):
    return redirect("/admin/")