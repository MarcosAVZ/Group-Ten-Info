# Generated by Django 4.2.3 on 2024-10-12 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(default='fotos_perfil/predeterminado.jpg', upload_to='fotos_perfil/'),
        ),
    ]
