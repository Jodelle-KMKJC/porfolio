from django.shortcuts import render, redirect
from .models import Gateau
from .forms import GateauForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

@login_required
def create_gateaux(request):
    if request.method == 'POST':
        form = GateauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GateauForm()
    return render(request, 'dashboard.html', {'form': form, 'user': request.user})

# Vue pour la page base.html
class BaseView(TemplateView):
    template_name = 'base.html'

# ✅ Vue pour la page d'accueil (corrigée)
class AccueilView(TemplateView):
    template_name = 'accueil.html'

# Vue pour la page À propos
class AProposView(TemplateView):
    template_name = 'propos.html'

# Vue pour la page Nos Gâteaux
class NosGateauxView(TemplateView):
    template_name = 'nos_gateaux.html'

# Vue pour la page Catégorie
class CategorieView(TemplateView):
    template_name = 'categorie.html'

# Vue pour la page Contact
class ContactView(TemplateView):
    template_name = 'contact.html'
