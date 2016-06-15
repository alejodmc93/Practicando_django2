from django.conf.urls import url
from .views import RegistrarRestaurante,ReportarRestaurante,EliminarRestaurante

from . import views


app_name = 'restaurantes'
urlpatterns = [

	url(r'^registrar/$', RegistrarRestaurante.as_view(), name="registrar_restaurante"),
	url(r'^reportar/$', ReportarRestaurante.as_view(), name="reportar_restaurante"),
	url(r'^reportar/(?P<pk>[0-9]+)$', EliminarRestaurante.as_view(), name="eliminar_restaurante"),
		
]