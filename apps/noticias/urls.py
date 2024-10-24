
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),
    
	path('crear/', views.Crear_noticia, name='crear'),
    
	path('editar/<int:pk>/', views.Editar_noticia, name='editar_noticia'), 
    
	path('eliminar/<int:pk>/', views.Eliminar_noticia, name='eliminar_noticia'),  

	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
	
    path('comentario/editar/<int:pk>/', views.Editar_comentario, name='editar_comentario'),
    
	path('comentario/eliminar/<int:pk>/', views.Eliminar_Comentario, name='eliminar_comentario'),

	path('denunciar/', views.Denunciar_Noticia, name='denunciar_noticia'),
    
	path('administrar/', views.administrar_denuncias, name='administrar_denuncias'),
    
    path('bloquear/<int:denuncia_id>/', views.bloquear_cuenta, name='bloquear_cuenta'),
]

