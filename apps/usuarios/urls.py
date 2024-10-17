from django.urls import path, include

from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),

    path('perfil/', views.perfil_usuario, name='perfil_usuario'),

    path('cambiar-foto-perfil/', views.cambiar_foto_perfil, name='cambiar_foto_perfil'),
]