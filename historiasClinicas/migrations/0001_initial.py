# Generated by Django 2.1.4 on 2018-12-07 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('empresa', models.CharField(max_length=100)),
                ('cargo_aspirado', models.CharField(max_length=150)),
                ('eps', models.CharField(max_length=100, verbose_name='EPS')),
                ('arl', models.CharField(max_length=100, verbose_name='ARL')),
                ('examen_actual', models.CharField(choices=[('preingreso', 'Pre-ingreso'), ('periodico', 'Periodico'), ('egreso', 'Egreso'), ('cambio labor', 'Cambio labor'), ('reincorporacion', 'Reincorporacion laboral'), ('rev paraclinicos', 'Rev. Paraclinicos'), ('manipulacion de alimentos', 'Manipulacion de alimentos')], max_length=50, verbose_name='Examen')),
                ('antecedentes_personales', models.TextField()),
                ('antecedentes_laborales', models.TextField()),
                ('antecedentes_familiares', models.TextField()),
                ('antecedentes_ginecobstetricos', models.TextField()),
                ('ta', models.CharField(max_length=9, verbose_name='TA')),
                ('fc', models.IntegerField(verbose_name='FC')),
                ('fr', models.IntegerField(verbose_name='FR')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('talla', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imc', models.DecimalField(decimal_places=2, max_digits=60, verbose_name='IMC')),
                ('cabeza_y_cuello', models.CharField(max_length=500)),
                ('sentidos', models.CharField(max_length=500)),
                ('cardiopulmonar', models.CharField(max_length=500)),
                ('abdomen', models.CharField(max_length=500)),
                ('osteomuscular', models.CharField(max_length=500)),
                ('neurologico', models.CharField(max_length=500)),
                ('esfera_mental', models.CharField(max_length=500)),
                ('valoracion_medica', models.CharField(choices=[('apto sin patologia', 'Apto para desempeñar el cargo sin patologia aparente'), ('apto con patologia', 'Apto para desempañar el cargo con patologia que no limita la labor'), ('apto con restricciones', 'Apto con restricciones o adaptaciones para la labor'), ('aplazado', 'Aplazado'), ('apto alturas', 'Apto para labor el alturas'), ('apto continuacion labor', 'Apto para continuar desempeñando su labor'), ('examen de retiro', 'Examen de retiro'), ('apto para manipulación de alimentos', 'Apto para manipulación de alimentos')], max_length=50, verbose_name='Concepto de valoracion medica')),
                ('secuela_acci_trab', models.CharField(choices=[('si', 'Si'), ('no', 'No')], max_length=2, verbose_name='Secuela accidente de trabajo')),
                ('enfer_pro', models.CharField(choices=[('si', 'Si'), ('no', 'No')], max_length=2, verbose_name='Enfermedad profesional')),
                ('enfer_rel_trabajo', models.CharField(choices=[('si', 'Si'), ('no', 'No')], max_length=2, verbose_name='Enfermedad relacionada con el trabajo')),
                ('fecha_dxco', models.DateField(blank=True, null=True, verbose_name='Fecha del diagnostico')),
                ('fecha_at', models.DateField(blank=True, null=True, verbose_name='Fecha accidente de trabajo')),
                ('resultados_laboratorio', models.TextField(verbose_name='Resultados de laboratorio')),
                ('restricciones_laborales', models.CharField(choices=[('no se encuentra', 'No se encuentra'), ('transitorias', 'Transitorias'), ('tiempo', 'Tiempo'), ('permanentes', 'Permanentes')], max_length=50)),
                ('remite', models.CharField(choices=[('ninguno', 'Ninguno'), ('se remite EPS', 'Se remite a EPS'), ('continuar manejo medico EPS', 'Continuar manejo medico por EPS'), ('se remite ARL', 'Se remite a ARL')], max_length=50, verbose_name='Se remite a')),
                ('otras', models.TextField(verbose_name='Recomendaciones para la empresa')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('ingreso_sis_epidem_ocup', models.CharField(choices=[('ergonomico', 'Ergonómico'), ('Psicosocial', 'Psicosocial'), ('auditivo', 'Autitivo'), ('visual', 'Visual'), ('respiratorio', 'Respitatorio'), ('biologico', 'Biológico'), ('quimico', 'Quimico'), ('accidente trabajo', 'Accidente de trabajo'), ('otro', 'Otro'), ('ninguno', 'Ninguno')], max_length=50, verbose_name='Ingresar al trabajador examinado al Sistema de Vigilancia Epidemiológica Ocupacional')),
            ],
        ),
        migrations.CreateModel(
            name='Cabecera',
            fields=[
                ('numero_historia', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='actualizacion',
            name='cabecera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historiasClinicas.Cabecera'),
        ),
    ]
