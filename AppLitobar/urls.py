from django.contrib import admin
from django.urls import path
from AppLitobar import views, views_clases


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("mascotas/", views.busqueda_mascota, name="mascotas"),
    path("cita/", views.cita_formulario, name="cita"), 
    path("apoderados/", views.apoderados_formulario, name="apoderado"),
    path("mascotas/", views.mascotas_formulario, name="mascotas"),
    path('buscar/', views.buscar, name="buscar"),
    path('login/', views_clases.login_request, name="Login"),
    path('acerca-de-mi/', views.about, name="acerca-de-mi"),
    path('nada-por-aca/', views.nada, name="nada-por-aca"),
]

urls_vistas_clases = [
    path('clases/lista/', views_clases.CitaListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views_clases.CitaDetalle.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.CitaCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views_clases.CitaUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views_clases.CitaDeleteView.as_view(), name='Delete'),


    path('clases/listaM/', views_clases.MascotasListView.as_view(), name='Lista'),
    path('clases/detalleM/<int:pk>/', views_clases.MascotasDetalle.as_view(), name='Detalle'),
    path('clases/nuevoM/', views_clases.MascotasCreateView.as_view(), name='Nuevo'),
    path('clases/editarM/<int:pk>', views_clases.MascotasUpdateView.as_view(), name='Editar'),
    path('clases/eliminarM/<int:pk>', views_clases.MascotasDeleteView.as_view(), name='Borrar'),
]

urlpatterns += urls_vistas_clases