
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pythonCode import panier as pan
from pythonCode import forms
from django.template import Context
from .models import Produit

def index(request):
    return HttpResponse("Alors, on a le covid?")

def panier(request):
    if request.method == "POST":
        pan.Update(request)
        return HttpResponseRedirect(reverse('commandes'))
    if request.method == "GET":
        c = list()
        for p in ["legume", "gateau", "laitpoudre", "huile", "sel", "semoule", "sucre", "cereale", "lingette", "savon", "farine", "riz", "pate", "eau", "lait"]:
            prix =  Produit.objects.get(name=p).prix
            q = request.session.get(p,0)
            c.append({"nom": p , "q" : q, "prixU": prix , "prixT" : float(prix) * int(q)})
        return render(request, "panier.html", {"produits" : c})
        
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
    c = list()
    e = list()
    i = 0
    for p in ["legume", "gateau", "laitpoudre", "huile", "sel", "semoule", "sucre", "cereale", "lingette", "savon", "farine", "riz", "pate", "eau", "lait"]:
            if i == 3:
                i = 0
                c.append(e)
                e = list()

            produit = Produit.objects.get(name=p)
            e.append({"name": p , "namePretty" : produit.name_Pretty, "prix": produit.prix , "desc" : produit.desc})
            i += 1
    return render(request, "listProduit.html", {"produits" : c})

def delPanier(request):
    pan.Delete(request)
    return HttpResponseRedirect(reverse("panier"))
