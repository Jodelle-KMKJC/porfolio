from django.urls import path
from .views import IndexView, ConnexionView, InscriptionView, ReceptionView, AdminDashboardView, VendeurDashboardView, ClientHomeView


urlpatterns = [
    path('', IndexView.as_view(), name='accueil'),
    path('start/', ReceptionView.as_view(), name='start'),
    path('connexion/', ConnexionView.as_view(), name='connexion'),
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('vendeur/dashboard/', VendeurDashboardView.as_view(), name='vendeur_dashboard'),
    path('client/home/', ClientHomeView.as_view(), name='client_home'),
]



