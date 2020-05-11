from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import ConfinAide.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
<<<<<<< HEAD
    path('deconnexion/', views.deconnexion, name='deconnexion')
=======
    path('commandes/', views.commandes, name='commandes'),
    path('panier/',views.panier, name='panier')
>>>>>>> d6f2f5008a9708aaca99a42ea826b782104906d1
]

urlpatterns += staticfiles_urlpatterns()