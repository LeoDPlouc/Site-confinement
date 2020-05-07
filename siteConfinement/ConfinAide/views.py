from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Alors, on a le covid?")

def connexion(request):
    return render(request, "connexion.html")

def inscription(request):
    return render(request, "inscription.html")    