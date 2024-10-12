from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):#
	pass
	#Foto de perfil
	foto_perfil = models.ImageField(upload_to='fotos_perfil/', default='fotos_perfil/predeterminado.jpg')
