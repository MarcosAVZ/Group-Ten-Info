<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
=======
from django.shortcuts import render, redirect
>>>>>>> marcos
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.noticias.models import Noticia
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import random

from .forms import RegistroForm
from django.contrib import messages
from .models import Usuario
from django.contrib.auth import authenticate, login

from .forms import CambiarFotoPerfilForm

# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'


@login_required
def perfil_usuario(request):
    # Obtener el usuario autenticado
    usuario = request.user 

    if usuario.bloqueado:
        messages.error(request, 'Su usuario ha sido bloqueado. Comuníquese con el admin para más detalles.')
        return redirect('login') 
    
    advertencia = usuario.advertencia 

    # Contar el número total de noticias
    total_noticias = Noticia.objects.count()

    # Filtrar las noticias del usuario autenticado
    noticias_usuario = Noticia.objects.filter(autor=usuario)

    # Seleccionar 5 noticias aleatorias si hay 5 o más
    if total_noticias >= 5:
        noticias_aleatorias = Noticia.objects.order_by('?')[:5]
    else:
        noticias_aleatorias = Noticia.objects.order_by('?')[:total_noticias]

    # Obtener la advertencia del usuario
    advertencia = usuario.advertencia  # Obtener la advertencia si existe

    # Renderizar la plantilla y pasar las noticias y la advertencia al contexto
    return render(request, 'usuarios/perfil.html', {
        'noticias': noticias_usuario,
        'noticias_aleatorias': noticias_aleatorias,
        'advertencia': advertencia,  # Pasar la advertencia al contexto
    })

@login_required
def advertir_o_bloquear_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    if request.method == 'POST':
        if 'advertir' in request.POST:
            advertencia = "Has recibido una advertencia."
            usuario.advertencia = advertencia
            usuario.save()
            print(f'Advertencia guardada: {usuario.advertencia}')  # Añade esta línea para debug
            messages.success(request, f'Advertencia enviada a {usuario.username}.')
        elif 'bloquear' in request.POST:
            usuario.bloqueado = True
            usuario.is_active = False
            usuario.save()
            messages.success(request, 'El usuario ha sido bloqueado. Comuníquese con el admin para más detalles.')
        return redirect('usuario:lista_usuarios')

    return render(request, 'usuarios/advertir_bloquear.html', {'usuario': usuario})

@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # O ajusta el filtro según tus necesidades
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        # Intentar obtener el usuario y verificar si está bloqueado
        try:
            user = Usuario.objects.get(username=username)
            if user.bloqueado:
                messages.error(request, 'Tu cuenta está bloqueada. Comunícate con el administrador.')
                return render(request, 'usuarios/login.html')  # Asegúrate de usar la plantilla correcta
            
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.advertencia:
                    messages.warning(request, f'Tienes una advertencia: {user.advertencia}')
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio
            else:
                messages.error(request, 'Credenciales inválidas.')
                return render(request, 'usuarios/login.html')  # Cambiar de redirect a render
    
        except Usuario.DoesNotExist:
            messages.error(request, 'Credenciales inválidas.')
            return render(request, 'usuarios/login.html')  # Cambiar de redirect a render  
    
    return render(request, 'usuarios/login.html')
def cambiar_foto_perfil(request):
    if request.method == 'POST':
        form = CambiarFotoPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil_usuario')  # Redirige a la página de perfil después de actualizar la foto
    else:
        form = CambiarFotoPerfilForm(instance=request.user)

    return render(request, 'usuarios/cambiar_foto_perfil.html', {'form': form})

