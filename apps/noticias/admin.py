from django.contrib import admin

from .models import Categoria, Noticia, Comentario

admin.site.register(Categoria)
admin.site.register(Noticia)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'noticia', 'fecha')
    search_fields = ('usuario__username', 'texto')
    list_filter = ('fecha', 'noticia')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for comentario in queryset:
            comentario.delete()