from django.shortcuts import render, redirect
from .models import Gateau
from .forms import GateauForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])  # <-- Ajoutez cette ligne
def contact_view(request):

    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')
        
        # Construire le sujet et le contenu de l'email
        subject_map = {
            'commande': 'Commande spéciale',
            'question': 'Question sur les produits',
            'livraison': 'Demande de livraison',
            'evenement': 'Organisation d\'événement',
            'autre': 'Autre demande'
        }
        email_subject = f"Contact Jodelle Patisserie: {subject_map.get(subject, 'Autre')}"
        
        email_body = f"""
        Nouveau message de contact:
        
        Nom: {name}
        Email: {email}
        Sujet: {subject_map.get(subject, 'Autre')}
        
        Message:
        {message_content}
        
        ---
        Cet email a été envoyé depuis le formulaire de contact du site Jodelle Patisserie.
        """
        
        try:
            # Envoyer l'email
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,  # Votre email d'envoi
                ['cabrellekamgaing@gmail.com'],  # Votre email de réception
                fail_silently=False,
            )
            
            # Message de succès
            messages.success(request, 'Votre message a été envoyé avec succès! Nous vous répondrons bientôt.')
            return redirect('contact')  # Rediriger vers la même page
            
        except Exception as e:
            # Message d'erreur
            messages.error(request, f"Une erreur s'est produite lors de l'envoi de votre message: {str(e)}")
            return redirect('contact')
    
    # Si GET, afficher la page normale
    return render(request, 'votre_template.html')  # Remplacez par votre template
    
@login_required
def create_gateaux(request):
    if request.method == 'POST':
        form = GateauForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GateauForm()
    return render(request, 'dashboard.html', {'form': form, 'user': request.user})

class NosGateauxView(TemplateView):
    template_name = 'cake/nos_gateaux.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gateaux'] = Gateau.objects.all()
        return context

class AProposView(TemplateView):
    template_name = 'cake/apropos.html'

class CategorieView(TemplateView):
    template_name = 'cake/categorie.html'

class ContactView(TemplateView):
    template_name = 'cake/contact.html'

class RetourView(TemplateView):
    template_name = 'cake/accueil.html'
