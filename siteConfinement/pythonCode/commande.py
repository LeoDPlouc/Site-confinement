
from ConfinAide.models import Client, commande_produit, Produit

def Validation(request):
    mail = request.session.get("id_mail",None)
    password = request.session.get("id_password",None)
    if(mail==None or password==None): return False
    
    id_client = (Client.objects.filter(mail=mail,password=password)).id_client
    produits = [o.name for o in Produit.objects.all()]
    for p in produits:
        tmp = request.session.get(p,0)
        while(tmp>0):
            new_commande = commande_produit(id_produit =p, id_client = id_client)
            new_commande.save()
            tmp=tmp-1
    return True
            
            