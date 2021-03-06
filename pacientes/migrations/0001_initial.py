# Generated by Django 2.1.4 on 2018-12-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=15)),
                ('segundo_nombre', models.CharField(blank=True, max_length=15)),
                ('primer_apellido', models.CharField(max_length=15)),
                ('segundo_apellido', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('estado_civil', models.CharField(choices=[('soltero', 'Soltero/a'), ('casado', 'Casado/a'), ('union libre', 'Union libre'), ('viudo', 'Viudo/a'), ('divorciado', 'Divorciado/a'), ('comprometido', 'Comprometido/a')], max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], default='sexo', max_length=15)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
