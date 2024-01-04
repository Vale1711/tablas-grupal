from django.shortcuts import render, redirect
from .models import Raza, Pais, Estado_Civil, Medicamento, Tipo_atencion
from django.contrib import messages


def index(request):
    razas = Raza.objects.all()
    return render(request, 'index.html', {'razas': razas, 'navbar': 'raza'})

def pais(request):
    paises = Pais.objects.all()
    return render(request, 'pais.html', {'paises': paises, 'navbar': 'pais'})

def estadocivil(request):
    estadociviles = Estado_Civil.objects.all()
    return render(request, 'estadocivil.html', {'estadociviles': estadociviles, 'navbar': 'estadocivil'})

def medicamento(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamento.html', {'medicamentos': medicamentos, 'navbar': 'medicamento'})

def tipoatencion(request):
    tiposatencion = Tipo_atencion.objects.all()
    return render(request, 'tipoatencion.html', {'tiposatencion': tiposatencion, 'navbar': 'tipoatencion'})

def guardarRaza(request):
    nombre_va=request.POST["nombre_va"]
    tamano_va=request.POST["tamano_va"]
    alimentacion_va=request.POST["alimentacion_va"]
    color_va=request.POST["color_va"]
    temperamento_va=request.POST["temperamento_va"]

    nuevaRaza=Raza.objects.create(nombre_va=nombre_va, tamano_va=tamano_va, alimentacion_va=alimentacion_va,
                                          color_va=color_va, temperamento_va=temperamento_va)
    messages.success(request, 'Cliente Guardado exitosamente')
    return redirect('/')

def guardarPais(request):
    nombre_pa_va=request.POST["nombre_pa_va"]
    capital_va=request.POST["capital_va"]
    poblacion_va=request.POST["poblacion_va"]
    idioma_va=request.POST["idioma_va"]
    moneda_va=request.POST["moneda_va"]

    nuevoPais=Pais.objects.create(nombre_pa_va=nombre_pa_va, capital_va=capital_va, poblacion_va=poblacion_va,
                                          idioma_va=idioma_va, moneda_va=moneda_va)
    messages.success(request, 'Cliente Guardado exitosamente')
    return redirect('/pais')

def guardarEstado(request):
    nombre_es_va=request.POST["nombre_es_va"]
    descripcion_va=request.POST["descripcion_va"]
    fecha_creacion_va=request.POST["fecha_creacion_va"]
    fecha_modificacion_va=request.POST["fecha_modificacion_va"]
    autor_va=request.POST["autor_va"]

    nuevoEstado=Estado_Civil.objects.create(nombre_es_va=nombre_es_va, descripcion_va=descripcion_va, fecha_creacion_va=fecha_creacion_va,
                                          fecha_modificacion_va=fecha_modificacion_va, autor_va=autor_va)
    messages.success(request, 'Cliente Guardado exitosamente')
    return redirect('/estadocivil')


def guardarMedicamento(request):
    nombre_me_va=request.POST["nombre_me_va"]
    descripcion_me_va=request.POST["descripcion_me_va"]
    fabricante_va=request.POST["fabricante_va"]
    precio_va=request.POST["precio_va"]
    fecha_caducidad_va=request.POST["fecha_caducidad_va"]

    nuevoMedicamento=Medicamento.objects.create(nombre_me_va=nombre_me_va, descripcion_me_va=descripcion_me_va, fabricante_va=fabricante_va,
                                          precio_va=precio_va, fecha_caducidad_va=fecha_caducidad_va)
    messages.success(request, 'Cliente Guardado exitosamente')
    return redirect('/medicamento')


def guardarAtencion(request):
    nombre_ti_va=request.POST["nombre_ti_va"]
    descripcion_ti_va=request.POST["descripcion_ti_va"]
    duracion_va=request.POST["duracion_va"]
    costo_va=request.POST["costo_va"]
    personal_asignado_va=request.POST["personal_asignado_va"]

    nuevoAtencion=Tipo_atencion.objects.create(nombre_ti_va=nombre_ti_va, descripcion_ti_va=descripcion_ti_va, duracion_va=duracion_va,
                                          costo_va=costo_va, personal_asignado_va=personal_asignado_va)
    messages.success(request, 'Cliente Guardado exitosamente')
    return redirect('/tipoatencion')


def eliminarRaza(request,codigo_va):
    razaEliminar=Raza.objects.get(codigo_va=codigo_va)
    razaEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/')

def eliminarEstado(request,codigo_es_va):
    estadoEliminar=Estado_Civil.objects.get(codigo_es_va=codigo_es_va)
    estadoEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/estadocivil')

def eliminarPais(request,codigo_pa_va):
    paisEliminar=Pais.objects.get(codigo_pa_va=codigo_pa_va)
    paisEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/pais')

def eliminarMedicamento(request,codigo_me_va):
    medicamentoEliminar=Medicamento.objects.get(codigo_me_va=codigo_me_va)
    medicamentoEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/medicamento')

def eliminarAtencion(request,codigo_ti_va):
    atencionEliminar=Tipo_atencion.objects.get(codigo_ti_va=codigo_ti_va)
    atencionEliminar.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('/tipoatencion')

def editarRaza(request, codigo_va):
    razaEditar=Raza.objects.get(codigo_va=codigo_va)
    return render(request, 'editarRaza.html', {'raza': razaEditar})

def procesarinformacionRaza(request):
    codigo_va=request.POST["codigo_va"]
    nombre_va=request.POST["nombre_va"]
    tamano_va=request.POST["tamano_va"]
    alimentacion_va=request.POST["alimentacion_va"]
    color_va=request.POST["color_va"]
    temperamento_va=request.POST["temperamento_va"]
    #Insertando datos mediante el ORM de DJANGO
    razaEditar=Raza.objects.get(codigo_va=codigo_va)
    razaEditar.nombre_va=nombre_va
    razaEditar.tamano_va=tamano_va
    razaEditar.alimentacion_va=alimentacion_va
    razaEditar.color_va=color_va
    razaEditar.temperamento_va=temperamento_va
    razaEditar.save()
    messages.success(request,
      'Cliente ACTUALIZADO Exitosamente')
    return redirect('/')

def editarPais(request, codigo_pa_va):
    paisEditar=Pais.objects.get(codigo_pa_va=codigo_pa_va)
    return render(request, 'editarPais.html', {'pais': paisEditar})

def procesarinformacionPais(request):
    codigo_pa_va=request.POST["codigo_pa_va"]
    nombre_pa_va=request.POST["nombre_pa_va"]
    capital_va=request.POST["capital_va"]
    poblacion_va=request.POST["poblacion_va"]
    idioma_va=request.POST["idioma_va"]
    moneda_va=request.POST["moneda_va"]
    #Insertando datos mediante el ORM de DJANGO
    paisEditar=Pais.objects.get(codigo_pa_va=codigo_pa_va)
    paisEditar.nombre_pa_va=nombre_pa_va
    paisEditar.capital_va=capital_va
    paisEditar.poblacion_va=poblacion_va
    paisEditar.idioma_va=idioma_va
    paisEditar.moneda_va=moneda_va
    paisEditar.save()
    messages.success(request,
      'Cliente ACTUALIZADO Exitosamente')
    return redirect('/pais')

def editarEstado(request, codigo_es_va):
    estadoEditar=Estado_Civil.objects.get(codigo_es_va=codigo_es_va)
    return render(request, 'editarEstado.html', {'estadocivil': estadoEditar})

def procesarinformacionEstado(request):
    codigo_es_va=request.POST["codigo_es_va"]
    nombre_es_va=request.POST["nombre_es_va"]
    descripcion_va=request.POST["descripcion_va"]
    fecha_creacion_va=request.POST["fecha_creacion_va"]
    fecha_modificacion_va=request.POST["fecha_modificacion_va"]
    autor_va=request.POST["autor_va"]
    #Insertando datos mediante el ORM de DJANGO
    estadoEditar=Estado_Civil.objects.get(codigo_es_va=codigo_es_va)
    estadoEditar.nombre_es_va=nombre_es_va
    estadoEditar.descripcion_va=descripcion_va
    estadoEditar.fecha_creacion_va=fecha_creacion_va
    estadoEditar.fecha_modificacion_va=fecha_modificacion_va
    estadoEditar.autor_va=autor_va
    estadoEditar.save()
    messages.success(request,
      'Cliente ACTUALIZADO Exitosamente')
    return redirect('/estadocivil')


def editarMedicamento(request, codigo_me_va):
    medicamentoEditar=Medicamento.objects.get(codigo_me_va=codigo_me_va)
    return render(request, 'editarMedicamento.html', {'medicamento': medicamentoEditar})

def procesarinformacionMedicamento(request):
    codigo_me_va=request.POST["codigo_me_va"]
    nombre_me_va=request.POST["nombre_me_va"]
    descripcion_me_va=request.POST["descripcion_me_va"]
    fabricante_va=request.POST["fabricante_va"]
    precio_va=request.POST["precio_va"]
    fecha_caducidad_va=request.POST["fecha_caducidad_va"]
    #Insertando datos mediante el ORM de DJANGO
    medicamentoEditar=Medicamento.objects.get(codigo_me_va=codigo_me_va)
    medicamentoEditar.nombre_me_va=nombre_me_va
    medicamentoEditar.descripcion_me_va=descripcion_me_va
    medicamentoEditar.fabricante_va=fabricante_va
    medicamentoEditar.precio_va=precio_va
    medicamentoEditar.fecha_caducidad_va=fecha_caducidad_va
    medicamentoEditar.save()
    messages.success(request,
      'Cliente ACTUALIZADO Exitosamente')
    return redirect('/medicamento')

def editarAtencion(request, codigo_ti_va):
    atencionEditar=Tipo_atencion.objects.get(codigo_ti_va=codigo_ti_va)
    return render(request, 'editarAtencion.html', {'tipoatencion': atencionEditar})

def procesarinformacionAtencion(request):
    codigo_ti_va=request.POST["codigo_ti_va"]
    nombre_ti_va=request.POST["nombre_ti_va"]
    descripcion_ti_va=request.POST["descripcion_ti_va"]
    duracion_va=request.POST["duracion_va"]
    costo_va=request.POST["costo_va"]
    personal_asignado_va=request.POST["personal_asignado_va"]
    #Insertando datos mediante el ORM de DJANGO
    atencionEditar=Tipo_atencion.objects.get(codigo_ti_va=codigo_ti_va)
    atencionEditar.nombre_ti_va=nombre_ti_va
    atencionEditar.descripcion_ti_va=descripcion_ti_va
    atencionEditar.duracion_va=duracion_va
    atencionEditar.costo_va=costo_va
    atencionEditar.personal_asignado_va=personal_asignado_va
    atencionEditar.save()
    messages.success(request,
      'Cliente ACTUALIZADO Exitosamente')
    return redirect('/tipoatencion')
