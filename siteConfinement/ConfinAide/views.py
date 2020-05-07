from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from ..pythonCode import panier


def index(request):
    return HttpResponse("Alors, on a le covid?")

def connexion(request):
    return render(request, "connexion.html")

def inscription(request):
    return render(request, "inscription.html")    

def panier(request):
    if request.method == "POST":
        panier.Update(request)
