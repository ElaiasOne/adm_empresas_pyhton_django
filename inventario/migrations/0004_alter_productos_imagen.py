# Generated by Django 4.2.6 on 2023-10-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_productos_imagen_productos_origen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos_imagenes/'),
        ),
    ]
