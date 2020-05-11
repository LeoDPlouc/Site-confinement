from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from ..pythonCode import panier
from django.contrib.auth import authenticate, get_user_model, login, logout

from .forms import UserLoginForm, UserRegisterForm

def index(request):
    return HttpResponse("Alors, on a le covid?")

#def connexion(request):
#    return render(request, "connexion.html")

#def inscription(request):
#    return render(request, "inscription.html")    

def panier(request):
    if request.method == "POST":
        panier.Update(request)
        
def connexion(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')
    
    context = {
        'form':form,
    }
    return render(request,"connexion.html",context)

def insciption(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)
        if next:
            return redirect(next)
        return redirect('/')
    
    context = {
        'form':form,
    }
    return render(request,"inscription.html",context)

def deconnexion(request):
    logout(request)
    return redirect('/')