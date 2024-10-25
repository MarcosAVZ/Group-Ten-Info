from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):#
	

	foto_perfil = models.ImageField(upload_to='fotos_perfil/', default='fotos_perfil/predeterminado.jpg')
	advertencia = models.TextField(blank=True, null=True)  # Campo para indicar si el usuario ha sido advertido
	bloqueado = models.BooleanField(default=False)  # Campo para indicar si el usuario está bloqueado
	
	def __str__(self):
		return self.username