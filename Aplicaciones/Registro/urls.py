from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pais/', views.pais, name='pais'),
    path('estadocivil/', views.estadocivil, name='estadocivil'),
    path('medicamento/', views.medicamento, name='medicamento'),
    path('tipoatencion/', views.tipoatencion, name='tipoatencion'),
    path('guardarRaza/', views.guardarRaza),
    path('guardarPais/', views.guardarPais, name='pais'),
    path('guardarEstado/', views.guardarEstado),
    path('guardarMedicamento/', views.guardarMedicamento),
    path('guardarAtencion/', views.guardarAtencion),
    path('eliminarRaza/<codigo_va>', views.eliminarRaza),
    path('eliminarEstado/<str:codigo_es_va>/', views.eliminarEstado, name='eliminarEstado'),
    path('eliminarPais/<codigo_pa_va>', views.eliminarPais),
    path('eliminarMedicamento/<codigo_me_va>', views.eliminarMedicamento),
    path('eliminarAtencion/<codigo_ti_va>', views.eliminarAtencion),
    path('editarRaza/<codigo_va>', views.editarRaza),
    path('procesarinformacionRaza/', views.procesarinformacionRaza),
    path('editarPais/<codigo_pa_va>', views.editarPais),
    path('procesarinformacionPais/', views.procesarinformacionPais),
    path('editarEstado/<codigo_es_va>', views.editarEstado),
    path('procesarinformacionEstado/', views.procesarinformacionEstado),
    path('editarMedicamento/<codigo_me_va>', views.editarMedicamento),
    path('procesarinformacionMedicamento/', views.procesarinformacionMedicamento),
    path('editarAtencion/<codigo_ti_va>', views.editarAtencion),
    path('procesarinformacionAtencion/', views.procesarinformacionAtencion),



]
