from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profil
from django.utils.translation import gettext_lazy as _


class ProfilInline(admin.StackedInline):
    model = Profil
    can_delete = False
    verbose_name_plural = 'Profil'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfilInline,)

    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('profil',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Informations personnelles'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Dates importantes'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
