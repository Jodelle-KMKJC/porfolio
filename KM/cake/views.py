from django.shortcuts import render, redirect
from .models import Gateau
from .forms import GateauForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

class AProposView(TemplateView):
    template_name = 'cake/apropos.html'

class NosGateauxView(TemplateView):
    template_name = 'cake/nos_gateaux.html'

class CategorieView(TemplateView):
    template_name = 'cake/categorie.html'

class ContactView(TemplateView):
    template_name = 'cake/contact.html'

class RetourView(TemplateView):
    template_name = 'cake/accueil.html'
