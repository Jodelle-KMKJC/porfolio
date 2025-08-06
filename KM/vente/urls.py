
from django.urls import path
from .views import IndexView, AcessView, WelcomeView, AboutView, OffersView, projectView, NotebookView, JoinView, TestView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('acess', AcessView.as_view(), name='acess'),
    path('welcome', WelcomeView.as_view(), name='welcome'),
    path('about', AboutView.as_view(), name='about'),
    path('offers', OffersView.as_view(), name='offers'),
    path('project', projectView.as_view(), name='project'),
    path('notebook', NotebookView.as_view(), name='notebook'),
    path('join', JoinView.as_view(), name='join'),
    path('test', TestView.as_view(), name='test'),


]