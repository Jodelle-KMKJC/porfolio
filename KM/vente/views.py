from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'acceuil.html'

class AcessView(TemplateView):
    template_name = 'connect.html'

class WelcomeView(TemplateView):
    template_name = 'acceuil.html'

class AboutView(TemplateView):
    template_name = 'A propos.html'

class OffersView(TemplateView):
    template_name = 'service.html'

class projectView(TemplateView):
    template_name = 'projet.html'

class NotebookView(TemplateView):
    template_name = 'blog.html'

class JoinView(TemplateView):
    template_name = 'contact.html'

class TestView(TemplateView):
    template_name = 'test.html'

