from django.shortcuts import render
from django.http import request
from permisos.models import Permiso
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View

def permisos(request):

	return render(request, "permisos/form.html")

def contador(request):
	nombre = request.GET['nombre']
	tipo = request.GET['tipo_ausencia']
	fecha_i = request.GET['fecha_desde']
	fecha_f = request.GET['fecha_hasta']
	dias = request.GET['numero_dias']

	user = User.objects.filter(username=nombre)
	permiso = Permiso(nombre= nombre, tipo_ausencia= tipo, fecha_desde=fecha_i, fecha_hasta=fecha_f, dias=dias)
	print(user)
	if (not user):
		user = User.objects.create_user(username=nombre)
		user.save()
	permiso.user = user	
	permiso.contador =+ 1
	permiso.save()

	#reporte = ReportePersonasPDF.
	return render(request, "permisos/informe.html")



