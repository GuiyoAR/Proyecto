# Generated by Django 4.0.5 on 2022-06-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_alter_paquete_activo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paquete',
            options={'verbose_name': 'paquete', 'verbose_name_plural': 'paquetes'},
        ),
        migrations.AlterField(
            model_name='paquete',
            name='Image_Set_1',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='paquete',
            name='Image_Set_2',
            field=models.ImageField(upload_to='media'),
        ),
    ]