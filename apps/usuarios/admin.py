from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    # Aquí puedes agregar las configuraciones que necesites
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.register(Usuario, CustomUserAdmin)