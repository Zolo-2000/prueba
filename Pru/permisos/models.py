from django.db import models
from django.contrib.auth.models import User


class Permiso(models.Model):
	tipos_ausencia = (
		(1, 'CARGO A VACACIONES'),
		(2, 'ENFERMEDAD'),		
		(3, 'COMPENSACION'),
		(4, 'CALAMIDAD'),		
		(5, 'PRESENTAR CERTIFICADO'),		
	)
	tipo_ausencia = models.PositiveSmallIntegerField(default=1, choices=tipos_ausencia)
	nombre = models.CharField(max_length=50)
	fecha_desde = models.DateTimeField()
	fecha_hasta = models.DateTimeField()
	dias = models.PositiveSmallIntegerField()
	contador = models.IntegerField(default=0)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __unicode__(self):
		return self.user

	def get_full_name(self):
		return self.user.get_full_name()