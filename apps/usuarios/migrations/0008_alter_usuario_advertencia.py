# Generated by Django 4.2.3 on 2024-10-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_usuario_advertencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='advertencia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
