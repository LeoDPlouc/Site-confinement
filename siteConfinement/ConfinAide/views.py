from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pythonCode import panier as pan

def index(request):
    return HttpResponse("Alors, on a le covid?") 

def panier(request):
    if request.method == "POST":
        pan.Update(request)
        return HttpResponseRedirect(reverse('commandes'))
    if request.method == "GET":
        return render(request, "panier.html")
        
def connexion(request):
    pass

def inscription(request):
    pass

def deconnexion(request):
    pass

def commandes(request):
    return render(request, "listProduit.html")
