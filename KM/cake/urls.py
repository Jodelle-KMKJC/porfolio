from django.urls import path
from .views import AProposView, NosGateauxView, CategorieView, ContactView, RetourView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('part/', AProposView.as_view(), name='apropos'),
    path('categorie/', CategorieView.as_view(), name='categorie'),
    path('nos_gateaux/', NosGateauxView.as_view(), name='nos_gateaux'),

    path('contact/', ContactView.as_view(), name='contact'),
    path('retour/', RetourView.as_view(), name='retour'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)