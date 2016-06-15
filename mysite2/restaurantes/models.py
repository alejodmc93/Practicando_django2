from django.db import models

class Restaurate(models.Model):
	nombre = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=8)

	status_active = 1
	status_deleted = 2

	status_choices = (
			(status_active,'activo'),
			(status_deleted,'eliminado'),
		)
	status = models.SmallIntegerField(
			choices = status_choices,
			default = status_active,
		)
	def __str__(self):
		return self.nombre

class Menu(models.Model):
	restaurate = models.ForeignKey(Restaurate)
	plato = models.CharField(max_length=100)
	def __str__(self):
		return self.plato

