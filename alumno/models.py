from __future__ import unicode_literals

from django.db import models


class alumno(models.Model):
	nombre = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	edad = models.IntegerField(max_length=2)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return "%s %s"%(self.nombre,self.apellidos)
