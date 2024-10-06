
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),

	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
	
    path('comentario/editar/<int:pk>/', views.Editar_comentario, name='editar_comentario'),
    
	path('comentario/eliminar/<int:pk>/', views.Eliminar_Comentario, name='eliminar_comentario'),

	# path('comentarios/<int:noticia_id>/', views.Listar_Comentarios, name='comentarios'),
]
