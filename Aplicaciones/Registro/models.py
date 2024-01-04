from django.db import models

# Create your models here.
class Raza(models.Model):
    codigo_va=models.AutoField(primary_key=True)
    nombre_va=models.CharField(max_length=50)
    tamano_va=models.CharField(max_length=50)
    alimentacion_va=models.CharField(max_length=150)
    color_va=models.CharField(max_length=50)
    temperamento_va=models.CharField(max_length=50)

class Pais(models.Model):
    codigo_pa_va=models.AutoField(primary_key=True)
    nombre_pa_va=models.CharField(max_length=50)
    capital_va=models.CharField(max_length=50)
    poblacion_va=models.IntegerField()
    idioma_va=models.CharField(max_length=50)
    moneda_va=models.CharField(max_length=50)

class Estado_Civil(models.Model):
    codigo_es_va=models.AutoField(primary_key=True)
    nombre_es_va=models.CharField(max_length=50)
    descripcion_va=models.CharField(max_length=150)
    fecha_creacion_va=models.DateField()
    fecha_modificacion_va=models.DateField()
    autor_va=models.CharField(max_length=50)

class Medicamento(models.Model):
    codigo_me_va=models.AutoField(primary_key=True)
    nombre_me_va=models.CharField(max_length=50)
    descripcion_me_va=models.CharField(max_length=150)
    fabricante_va=models.CharField(max_length=150)
    precio_va=models.CharField(max_length=50)
    fecha_caducidad_va=models.DateField()

class Tipo_atencion(models.Model):
    codigo_ti_va=models.AutoField(primary_key=True)
    nombre_ti_va=models.CharField(max_length=50)
    descripcion_ti_va=models.CharField(max_length=150)
    duracion_va=models.CharField(max_length=50)
    costo_va=models.CharField(max_length=50)
    personal_asignado_va=models.CharField(max_length=150)
