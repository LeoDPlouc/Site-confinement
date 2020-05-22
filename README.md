# ConfinAide

ConfinAide est une platerforme permettant aux famille de signaler leur besoin en nourriture

## Installation

Télécharger le dêpot sur [github](https://github.com/LeoDPlouc/Site-confinement)

Dans un terminal qui se situe dans le dossier principal executer: 

Linux:
```console
PathToProject$ cd siteConfinement/
```
Windows:
```console
PathToProject> cd siteConfinement/
```

Une fois ceci fait vous devriez être dans le repertoire d'un fichier nommé: "`manage.py`"

Afin de lancer le serveur, il suffit de lancer la commande suivante:

Linux:
```console
PathToProject$ python manage.py runserver
```
Windows:
```console
PathToProject> py manage.py runserver
```
Et voilà pour acceder au site il suffit de se rendre `localhost:8000/ConfinAide/connexion/`

## Administrateur

Afin de gérer le côté administrateur de l'application il faudra créé un compte, pour cela il faut de nouveau se rendre au niveau du fichier `manage.py` et executer:

Linux:
```console
PathToProject$ python manage.py createsuperuser
```
Windows:
```console
PathToProject> py manage.py createsuperuser
```

Une fois ceci fait il sufit de suivre les instructions et de se connecter dans l'interface d'administration: `localhost:8000/admin/`

Depuis cette interface vous pouvez ajouter/supprimer un produit, ajouter/supprimer un client, approuver ou refuser un commande très facilement.