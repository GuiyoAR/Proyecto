# Generated by Django 4.0.5 on 2022-07-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_alter_paquete_precio_publico'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='Image_Set_3',
            field=models.ImageField(default='default.jpg', upload_to='pack_profile'),
        ),
        migrations.AddField(
            model_name='paquete',
            name='Image_Set_4',
            field=models.ImageField(default='default.jpg', upload_to='pack_profile'),
        ),
        migrations.AlterField(
            model_name='paquete',
            name='Image_Set_1',
            field=models.ImageField(default='default.jpg', upload_to='pack_profile'),
        ),
        migrations.AlterField(
            model_name='paquete',
            name='Image_Set_2',
            field=models.ImageField(default='default.jpg', upload_to='pack_profile'),
        ),
    ]
