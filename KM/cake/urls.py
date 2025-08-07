from django.urls import path
from . import views
from .views import BaseView, AcceuilView, AProposView, NosGateauxView, CategorieView, ContactView

urlpatterns = [
    path('', views.start, name='start'),
    path('base/', BaseView.as_view(), name='base'),
    path('acceuil/', AccueilView.as_view(), name='acceuil'),
    path('propos/', views.Apropos_view, name='propos'),
    path('nos-gateaux/', NosGateauxView.as_view(), name='nos_gateaux'),
    path('categorie/', CategorieView.as_view(), name='categorie'),
    path('contact/', ContactView.as_view(), name='contact'),
]
