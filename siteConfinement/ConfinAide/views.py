
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from ..pythonCode import panier, forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pythonCode import panier as pan


from .forms import UserLoginForm, UserRegisterForm

def index(request):
    return HttpResponse("Alors, on a le covid?")

def panier(request):
    if request.method == "POST":

        panier.Update(request)
        
def connexion(request):
    if request.method == "POST":
        test = forms.Verification(request)
        if(test):
            HttpResponseRedirect(reverse("commandes"))
        else:
            HttpResponseRedirect(reverse("connexion"))
            
    
def insciption(request):
    if request.method == "POST":
        test = forms.Inscription(request)
        if(test):
            HttpResponseRedirect(reverse("commandes"))
        else:
            HttpResponseRedirect(reverse("inscription"))

def deconnexion(request):
    if request.method == "POST":
        forms.deconnexion(request)
        HttpResponseRedirect(reverse("connexion"))

def commandes(request):
    return render(request, "listProduit.html")

