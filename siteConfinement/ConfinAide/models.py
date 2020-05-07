from django.db import models

class Client(models.Model):
    id_client = models.BigIntegerField(primary_key=True)
    password = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 50)
    nom = models.CharField(max_length = 20, null = True)
    tel = models.CharField(max_length = 20, null = True)
    adresse = models.CharField(max_length = 20, null = True)
    
class Produit(models.Model):
    id_produit = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20, null = True)
    
class commande_produit(models.Model):
    id_commande_produit = models.BigIntegerField(primary_key = True)
    id_produit = models.ForeignKey(Produit, on_delete = models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete = models.CASCADE)
    confirm = models.BooleanField(default = False)
    description = models.CharField(max_length = 20)