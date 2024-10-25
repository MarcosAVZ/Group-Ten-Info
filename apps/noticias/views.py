from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm, NoticiaForm, DenunciaForm
from django.db.models import Q

from .models import Noticia, Categoria, Comentario, Denuncia

from django.urls import reverse_lazy
from apps.usuarios.models import Usuario
from django.contrib import messages

def Listar_Noticias(request):
    contexto = {}

    # Obtener parámetros de filtro
    id_categoria = request.GET.get('categoria', None)
    ordenar = request.GET.get('ordenar', None)
    mis_noticias = request.GET.get('mis_noticias', 'false')
    id_autor = request.GET.get('autor', None) 

    # Filtrar por categoría 
    if id_categoria:
        noticias = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        noticias = Noticia.objects.all() 

    if mis_noticias == 'true' and request.user.is_authenticated:
        noticias = noticias.filter(autor=request.user)
    elif id_autor:
        noticias = noticias.filter(autor_id=id_autor)

    # Ordenar por antigüedad o título si se proporciona el parámetro
    if ordenar == 'antiguedad_asc':
        noticias = noticias.order_by('fecha')  # Orden ascendente por fecha (antiguo a reciente)
    elif ordenar == 'antiguedad_desc':
        noticias = noticias.order_by('-fecha')  # Orden descendente por fecha (reciente a antiguo)
    elif ordenar == 'titulo_asc':
        noticias = noticias.order_by('titulo')  # Orden ascendente por título (alfabético)
    elif ordenar == 'titulo_desc':
        noticias = noticias.order_by('-titulo')  # Orden descendente por título (alfabético inverso)

    # Añadir las noticias y categorías al contexto
    contexto['noticias'] = noticias
    contexto['categorias'] = Categoria.objects.all().order_by('nombre')
    contexto['autores'] = Usuario.objects.all()

    return render(request, 'noticias/listar.html', contexto)

@login_required
def Crear_noticia(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        cuerpo = request.POST['cuerpo']
        imagen = request.FILES['imagen']
        autor = request.user
        categoria_noticia_id = request.POST['categoria_noticia']
        categoria_noticia = Categoria.objects.get(pk=categoria_noticia_id)
        
        noticia = Noticia(
            titulo=titulo,
            cuerpo=cuerpo,
            imagen=imagen,
            autor=autor,
            categoria_noticia=categoria_noticia
        )
        noticia.save()
        return redirect('noticias:listar')  # Redirige a la lista de noticias

    categorias = Categoria.objects.all()
    noticias = Noticia.objects.all()
    return render(request, 'noticias/listar.html', {'categorias': categorias, 'noticias': noticias})

@login_required
def Editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    categorias = Categoria.objects.all() 
    
    if request.method == 'POST':
        noticia.titulo = request.POST['titulo']
        noticia.cuerpo = request.POST['cuerpo']
        if 'imagen' in request.FILES:
            noticia.imagen = request.FILES['imagen']
        noticia.categoria_noticia_id = request.POST['categoria_noticia']
        noticia.save()
        return redirect('noticias:detalle', pk=noticia.pk)

    return render(request, 'noticias/editar_noticia.html',  {'noticia': noticia, 'categorias': categorias})

@login_required
def Eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias:listar')
    return render(request, 'noticias/eliminar_noticia.html', {'noticia': noticia})



def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):
	
	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

@login_required
def Eliminar_Comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    
    if request.user == comentario.usuario or request.user.is_superuser:  # Permitir al admin eliminar
        comentario.delete()
        return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': comentario.noticia.pk}))
    
    return HttpResponseForbidden("No puedes eliminar este comentario.")


@login_required
def Editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, id=pk)
    noticia_id = comentario.noticia.id  # Obtener el ID de la noticia

    # Verificar si el usuario que intenta editar el comentario es el autor
    if request.user != comentario.usuario and not request.user.is_superuser:
        return redirect('/Noticias/detalle.html')  # Cambia esto a la vista adecuada

    if request.method == 'POST':
        nuevo_texto = request.POST.get('comentario')  # Obtener el nuevo texto
        if nuevo_texto:  # Asegurarse de que no esté vacío
            comentario.texto = nuevo_texto  # Asignar el nuevo texto
            comentario.save()  # Guardar los cambios
        return redirect(f'/Noticias/Detalle/{noticia_id}')  # Redirigir a la vista de detalle de la noticia
    else:
        return redirect(f'/Noticias/Detalle/{noticia_id}') 

@login_required
def Denunciar_Noticia(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id) 
    print("Método de la solicitud:", request.method)  # Esto te dirá si es GET o POST
    if request.method == 'POST':

        form = DenunciaForm(request.POST)
        if form.is_valid():
            print("Formulario válido, redirigiendo a denuncia_exitosa...")
            motivo = form.cleaned_data['motivo']
            # Guardar la denuncia en la base de datos
            Denuncia.objects.create(usuario=request.user, noticia=noticia, motivo=motivo)

            # Mensaje de éxito
            messages.success(request, 'Denuncia realizada con éxito.')
            return redirect('noticias:denuncia_exitosa')  # Redirigir a una página de éxito
    else:
        form = DenunciaForm()

    return render(request, 'noticias/denunciar_noticia.html', {'form': form, 'noticia': noticia})

def denuncia_exitosa(request):
    
    return render(request, 'noticias/denuncia_exitosa.html')


#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''