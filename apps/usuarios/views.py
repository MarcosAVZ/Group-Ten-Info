from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.noticias.models import Noticia
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import random

from .forms import RegistroForm

# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'


@login_required
def perfil_usuario(request):
    # Contar el número total de noticias
    total_noticias = Noticia.objects.count()

    # Filtrar las noticias del usuario autenticado
    noticias_usuario = Noticia.objects.filter(autor=request.user)

    # Seleccionar 5 noticias aleatorias si hay 5 o más
    if total_noticias >= 5:
        noticias_aleatorias = Noticia.objects.order_by('?')[:5]
    else:
        noticias_aleatorias = Noticia.objects.order_by('?')[:total_noticias]

    # Renderizar la plantilla y pasar las noticias al contexto
    return render(request, 'usuarios/perfil.html', {
        'noticias': noticias_usuario,
        'noticias_aleatorias': noticias_aleatorias,
    })
