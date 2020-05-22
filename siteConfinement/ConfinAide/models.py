from django.db import models

class Client(models.Model):
    id_client = models.AutoField(primary_key=True, )
    password = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 50)
    nom = models.CharField(max_length = 20, null = True)
    prenom = models.CharField(max_length = 20, null=True)
    tel = models.CharField(max_length = 20, null = True)
    adresse = models.CharField(max_length = 20, null = True)
    nbr_personne = models.CharField(max_length=2, null=True)
    
class Produit(models.Model):
    name = models.CharField(primary_key = True, max_length = 20)
    name_Pretty = models.CharField(max_length = 50)
    prix = models.FloatField()
    desc = models.CharField(max_length = 250)
    
class commande_produit(models.Model):
    id_commande_produit = models.BigIntegerField(primary_key = True)
    name_produit = models.ManyToManyField(Produit)
    id_client = models.ForeignKey(Client, on_delete = models.CASCADE)
    confirm = models.BooleanField(default = False)
    description = models.CharField(max_length = 20)