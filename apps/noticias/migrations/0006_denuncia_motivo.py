# Generated by Django 4.2.3 on 2024-10-12 00:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_alter_comentario_options_noticia_autor_denuncia'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='motivo',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
