from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import Profil
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
# Page d'accueil
class IndexView(TemplateView):
    template_name = 'main.html'

# Vérifications pour les types d'utilisateurs
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

def is_vendeur(user):
    return user.is_authenticated and user.is_staff

def is_client(user):
    if user.is_authenticated and not user.is_staff and not user.is_superuser:
        try:
            return user.profil.user_type == 'client'
        except Profil.DoesNotExist:
            Profil.objects.create(user=user, user_type='client')
            return True
    return False

class ConnexionView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return reverse_lazy('admin_dashboard')
            elif user.is_staff:
                return reverse_lazy('vendeur_dashboard')
            else:
                try:
                    profil = user.profil
                    if profil.user_type == 'client':
                        return reverse_lazy('client_home')
                except Profil.DoesNotExist:
                    Profil.objects.create(user=user, user_type='client')
                    return reverse_lazy('client_home')
        return reverse_lazy('start')

class InscriptionView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profil.objects.create(user=user, user_type='client')
            return redirect('connexion')
        return render(request, 'register.html', {'form': form})

class ReceptionView(View):
    def get(self, request):
        return render(request, 'start.html')

@method_decorator(user_passes_test(is_superuser, login_url='start'), name='dispatch')
class AdminDashboardView(TemplateView):
    template_name = 'admin_dashboard.html'

@method_decorator(user_passes_test(is_vendeur, login_url='start'), name='dispatch')
class VendeurDashboardView(TemplateView):
    template_name = 'vendeur_dashboard.html'

@method_decorator(user_passes_test(is_client, login_url='start'), name='dispatch')
class ClientHomeView(TemplateView):
    template_name = 'client_home.html'