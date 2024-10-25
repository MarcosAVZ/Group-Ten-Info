from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = Usuario
    # Aquí puedes agregar las configuraciones que necesites
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    actions = ['advertir_usuario', 'bloquear_usuario', 'desbloquear_usuario']  # Agregar acciones

    def advertir_usuario(self, request, queryset):
        """Enviar una advertencia a los usuarios seleccionados."""
        for usuario in queryset:
            usuario.advertencia = "Has recibido una advertencia."  # Asigna una advertencia
            usuario.save()
            # Aquí podrías guardar la advertencia en un modelo, si es necesario
            messages.success(request, f'Se ha enviado una advertencia a {usuario.username}.')
        self.message_user(request, _("Advertencia enviada a los usuarios seleccionados."))

    advertir_usuario.short_description = 'Advertir usuarios seleccionados'  # Texto que se muestra en el admin

    def bloquear_usuario(self, request, queryset):
        """Bloquear a los usuarios seleccionados."""
        for usuario in queryset:
            usuario.is_active = False 
            usuario.bloqueado = True
            usuario.save()
            messages.success(request, f'El usuario {usuario.username} ha sido bloqueado.')
        self.message_user(request, _("Usuarios seleccionados han sido bloqueados."))

    bloquear_usuario.short_description = 'Bloquear usuarios seleccionados'  # Texto que se muestra en el admin

    def desbloquear_usuario(self, request, queryset):
        """Desbloquear a los usuarios seleccionados."""
        for usuario in queryset:
            usuario.is_active = True 
            usuario.bloqueado = False 
            usuario.save()
            messages.success(request, f'El usuario {usuario.username} ha sido desbloqueado.')
        self.message_user(request, _("Usuarios seleccionados han sido desbloqueados."))

    desbloquear_usuario.short_description = 'Desbloquear usuarios seleccionados'  # Texto que se muestra en el admin
admin.site.register(Usuario, CustomUserAdmin)