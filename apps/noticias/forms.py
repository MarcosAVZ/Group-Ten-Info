
from django import forms
from .models import Comentario, Noticia

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'imagen', 'categoria_noticia'] 

class DenunciaForm(forms.Form):
    titulo = forms.CharField(label='Título de la Noticia', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Ingresa el título de la noticia'
    }))
    url_noticia = forms.URLField(label='URL de la Noticia', widget=forms.URLInput(attrs={
        'placeholder': 'https://ejemplo.com/noticia'
    }))
    descripcion = forms.CharField(label='Descripción de la Denuncia', widget=forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Describe el motivo de la denuncia'
    }))
    tipo_denuncia = forms.ChoiceField(label='Tipo de Denuncia', choices=[
        ('falsa', 'Noticia Falsa'),
        ('engañosa', 'Contenido Engañoso'),
        ('plagio', 'Plagio'),
        ('otro', 'Otro')
    ])