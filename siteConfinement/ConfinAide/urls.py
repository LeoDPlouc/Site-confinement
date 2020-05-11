from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import ConfinAide.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
]

urlpatterns += staticfiles_urlpatterns()