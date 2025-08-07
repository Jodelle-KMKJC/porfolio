from django.urls import path
from . import views
from .views import BaseView, AccueilView, AProposView, NosGateauxView, CategorieView, ContactView

urlpatterns = [

    path('', IndexView.as_view(), name='accueil'),
    path('a-propos/', AProposView.as_view(), name='propos'),
    path('nos-gateaux/', NosGateauxView.as_view(), name='nos_gateaux'),
    path('categorie/', CategorieView.as_view(), name='categorie'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('connexion/', ConnexionView.as_view(), name='connexion'),
]
