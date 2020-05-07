from django.db import models

class Client(models.Model):
    id_client = models.BigIntegerField(primary_key=True)
    password = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 50)
    nom = models.CharField(max_length = 20, null = True)
    tel = models.CharField(max_length = 20, null = True)
    adresse = models.CharField(max_length = 20, null = True)
