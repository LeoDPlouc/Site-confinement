from django.http import HttpRequest
from django.contrib.auth import authenticate, login, get_user_model
from django import forms
from django import models
from Client.models import Client



def Verification(request):
    mail = request.POST.get("mail",request.session.get("id_mail",None))
    password = request.POST.get("password",request.session.get("id_password",None))
    if(mail == None or password == None): return False
    test = Client.objects.filter(mail=mail,password=password)
    if(len(test)!=0):
        request.session["id_mail"]=str(mail)
        request.session["id_password"]=str(password)
        return True
    else: return False
        
    
def Insciption (request):
    name = request.POST["name-input-field"]
    first_name = request.POST["firstname-input-field"]
    mail = request.POST["email-input-field"]
    adress = request.POST["adress-input-field"]
    tel = request.POST["name-input-field"]
    password = request.POST["password-input-field"]
    password2 = request.POST["repeat-password-field"]
    
    if(password!=password2):
        return False
    else:
        new_client = Client(nom=name,prenom=first_name,mail=mail,adresse=adress,tel=tel,password=password)
        new_client.save()
        request.session["id_mail"]=str(mail)
        request.session["id_password"]=str(password)
        return True
    
    
def Deconnexion(request):
    request.session.delattr("id_mail")
    request.session.delattr("id_password")
    





#def Connexion(request):
#    username = request.POST['email']
#    password = request.POST['password']
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        login(request, user)
        # Redirect to a success page.
#        ...
#    else:
        # Return an 'invalid login' error message.
#        ...

