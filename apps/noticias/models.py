from django.db import models
from apps.usuarios.models import Usuario
from django.conf import settings

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):
	titulo = models.CharField(max_length = 150)
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'noticias')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.noticia}->{self.texto}"

class Denuncia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    motivo = models.TextField(max_length=1500)  # Motivo de la denuncia, ajuste según necesidad
    

    def __str__(self):
        return f'Denuncia de {self.usuario.username} sobre "{self.noticia.titulo}"'