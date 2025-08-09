from django.contrib import admin
from .models import Gateau

@admin.register(Gateau)
class GateauAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix', 'disponibilite')
    search_fields = ('nom', 'categorie')
    list_filter = ('categorie', 'disponibilite')
    ordering = ('nom',)

    fieldsets = (
        (None, {
            'fields': ('nom', 'description', 'prix', 'image', 'categorie', 'disponibilite', 'avis')
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return True

from django.contrib import admin
from .models import Gateau
