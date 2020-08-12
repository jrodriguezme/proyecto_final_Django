from django.urls import path
from . import views

app_name = 'reporte' 

urlpatterns = [
	path('reserva',views.reserva, name='reserva'),
	path('reserva/<int:pk>/',views.detalles.as_view(), name='detalles_reserva'),
	path('reserva/agregar/', views.agregar.as_view(), name='agregar_reserva'),
	path('reserva/listar', views.listar.as_view(), name='listar_reserva'),
	path('reserva/<int:pk>/modificar/', views.modificar.as_view(template_name='reporte/reserva_update.html'), name='modificar_reserva'),
	path('reserva/<int:pk>/borrar/', views.eliminar.as_view(), name='eliminar_reserva'),
	path('reserva/modificar',views.modificar2,name='editar_reserva'),
	path('reserva/borrar',views.eliminar2,name='borrar_reserva')
]
