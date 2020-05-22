
from ConfinAide.models import Client, commande_produit

def Validation(request):
    mail = request.session.get("id_mail",None)
    password = request.session.get("id_password",None)
    if(mail==None or password==None): return False
    
    id_client = (Client.objects.filter(mail=mail,password=password)).id_client
    produits = ["legume","gateau","laitpoudre","huile","sel","semoule","sucre","cereale","lingette","savon","farine","riz","pate","eau","lait"]
    for p in produits:
        tmp = request.session.get(p,0)
        while(tmp>0):
            new_commande = commande_produit(id_produit =p, id_client = id_client)
            new_commande.save()
            tmp=tmp-1
    return True
            
            