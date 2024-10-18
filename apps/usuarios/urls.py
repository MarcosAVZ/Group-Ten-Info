from django.urls import path, include

from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),

    path('login/', views.login_view, name='login'),

    path('perfil/', views.perfil_usuario, name='perfil_usuario'),

    path('advertir_o_bloquear/<int:usuario_id>/', views.advertir_o_bloquear_usuario, name='advertir_o_bloquear'),

    path('lista/', views.lista_usuarios, name='lista_usuarios'),  # URL para listar usuarios
    path('cambiar-foto-perfil/', views.cambiar_foto_perfil, name='cambiar_foto_perfil'),
]