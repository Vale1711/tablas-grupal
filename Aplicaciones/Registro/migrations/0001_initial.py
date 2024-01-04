# Generated by Django 4.2.7 on 2024-01-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Civil',
            fields=[
                ('codigo_es_va', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_es_va', models.CharField(max_length=50)),
                ('descripcion_va', models.CharField(max_length=150)),
                ('fecha_creacion_va', models.DateField()),
                ('fecha_modificacion_va', models.DateField()),
                ('autor_va', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('codigo_me_va', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_me_va', models.CharField(max_length=50)),
                ('descripcion_me_va', models.CharField(max_length=150)),
                ('fabricante_va', models.CharField(max_length=150)),
                ('precio_va', models.FloatField()),
                ('fecha_caducidad_va', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('codigo_pa_va', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pa_va', models.CharField(max_length=50)),
                ('capital_va', models.CharField(max_length=50)),
                ('poblacion_va', models.IntegerField()),
                ('idioma_va', models.CharField(max_length=50)),
                ('moneda_va', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('codigo_va', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_va', models.CharField(max_length=50)),
                ('tamano_va', models.CharField(max_length=50)),
                ('alimentacion_va', models.CharField(max_length=150)),
                ('color_va', models.CharField(max_length=50)),
                ('temperamento_va', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_atencion',
            fields=[
                ('codigo_ti_va', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ti_va', models.CharField(max_length=50)),
                ('descripcion_ti_va', models.CharField(max_length=150)),
                ('duracion_va', models.CharField(max_length=50)),
                ('costo_va', models.FloatField()),
                ('personal_asignado_va', models.CharField(max_length=150)),
            ],
        ),
    ]