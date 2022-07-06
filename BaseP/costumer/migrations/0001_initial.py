# Generated by Django 4.0.5 on 2022-06-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('pasaporte', models.IntegerField()),
                ('vencimiento', models.DateField()),
                ('dni', models.IntegerField()),
                ('domicilio', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
