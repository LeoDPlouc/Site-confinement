
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pythonCode import panier as pan
from pythonCode import forms

def index(request):
    return HttpResponse("Alors, on a le covid?")

def panier(request):
    if request.method == "POST":
        pan.Update(request)
        return HttpResponseRedirect(reverse('commandes'))
    if request.method == "GET":
        return render(request, "panier.html")
        
def connexion(request):
    test = forms.Verification(request)
    if request.method == "POST":
        if test:
            return HttpResponseRedirect(reverse("commandes"))
        else:
            return HttpResponseRedirect(reverse("connexion"))
    if request.method == "GET":
        if test: return HttpResponseRedirect(reverse("commandes"))
        else: return render(request, "connexion.html")
            
    
def inscription(request):
    if request.method == "POST":
        test = forms.Inscription(request)
        if(test):
            return HttpResponseRedirect(reverse("commandes"))
        else:
            return HttpResponseRedirect(reverse("inscription"))
    if request.method == "GET":
        return render(request, "inscription.html")

def deconnexion(request):
    if request.method == "GET":
        forms.Deconnexion(request)
        return HttpResponseRedirect(reverse("connexion"))

def commandes(request):
    return render(request, "listProduit.html")
