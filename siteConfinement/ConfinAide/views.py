from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pythonCode import panier as pan


def index(request):
    return HttpResponse("Alors, on a le covid?")

def connexion(request):
    return render(request, "connexion.html")

def inscription(request):
    return render(request, "inscription.html")    

def panier(request):
    if request.method == "POST":
        pan.Update(request)
        return HttpResponseRedirect(reverse('commandes'))
        
def commandes(request):
    return render(request, "listProduit.html")