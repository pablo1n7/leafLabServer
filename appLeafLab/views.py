#! /usr/bin/python
# -*- coding: UTF-8-*-

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import json
import socket
import ipdb
from models import *

# Create your views here.

elementosSimples = {"imagenVisita":ImagenVisita,"punto":Punto,"valor":Valor,"planta":Planta,"ejemplar":Ejemplar,"visita":Visita,"transecta":Transecta,"campania":Campania,"tipoEjemplar":TipoEjemplar,"propiedad":Propiedad,"especie":Especie,"suelo":TipoSuelo,"dist":DistribucionGeografica,"familia":Familia ,"forma":FormaBiologica,"tipo":TipoBiologico,"estado":EstadoDeConservacion}

def index(request):
	return render_to_response('views/index.html')

def dataBase(request):
	formasBiologicas = FormaBiologica.objects.all()
	tiposBiologicos = TipoBiologico.objects.all()
	estadosConservacion = EstadoDeConservacion.objects.all()
	familias = Familia.objects.all()
	distribucionesGeograficas = DistribucionGeografica.objects.all()
	tiposSuelo = TipoSuelo.objects.all()
	especies = Especie.objects.all()
	return render_to_response('views/baseDatos.html',{"especies":especies[1:],"familias":familias[1:],"distribucionesGeograficas":distribucionesGeograficas[1:],"tiposSuelo":tiposSuelo[1:],"formasBiologicas":formasBiologicas[1:],"tiposBiologicos":tiposBiologicos[1:],"estadosConservacion":estadosConservacion[1:]})



def statistics(request):
	return render_to_response('views/estadisticas.html')

def about(request):
	return render_to_response('views/about.html')

def campain(request):
	return render_to_response('views/campanias.html')

def administracionDeDatos(request):
	return render_to_response('views/AdministracionDeDatos.html')

@csrf_exempt
def sincronizar(request):
	# if request.is_ajax():
	if request.method == 'GET':
		#Elementos que solo se sincronizando en un sentido.(del servidor hacia la aplicacion)
		usuario = request.GET.get("identidad")
		tipoElemento = request.GET.get("nombre")
		return HttpResponse(elementosSimples[tipoElemento].obtenerElementos())	
	else:
		usuario = request.POST.get("identidad")
		tipoElemento = request.POST.get("nombre")
		datos = json.loads(request.POST.get("datos"))
		return HttpResponse(elementosSimples[tipoElemento].obtenerElementos(datos))	


@csrf_exempt
def identidad(request):
	nombrePC = socket.gethostname()
	ipPC = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
	jsondata = json.dumps({'nombrePC': nombrePC,'ip':ipPC})
	return HttpResponse(jsondata)

@csrf_exempt
def altaElementoSimple(request):
	#ipdb.set_trace()
	if request.is_ajax():
		tipoElemento = request.POST.get('tipo','') 
		identificador=request.POST.get('id','')
		if int(identificador)==-1:
			elemento = elementosSimples[tipoElemento](nombre=request.POST.get('nombre',''))
		else:
			elemento = elementosSimples[tipoElemento].objects.get(id=identificador);
			elemento.nombre = request.POST.get('nombre','');
		if tipoElemento == "especie":
			elemento.construir(request.POST);
		jsondata = json.dumps(elemento.salvar())
		return HttpResponse(jsondata)

@csrf_exempt
def bajaElementoSimple(request):
	if request.is_ajax():
		identificador = request.POST.get('id','')
		tipoElemento = request.POST.get('tipo','') 
		elemento = elementosSimples[tipoElemento].objects.get(id=identificador)
		jsondata = json.dumps(elemento.eliminar())
		return HttpResponse(jsondata)




@csrf_exempt
def subirImagenes(request):	
	#ipdb.set_trace()
	visita = Visita.objects.get(id=request.POST.get('visita'))
	file_obj = request.FILES['imagen']
	ruta = '/'.join([settings.IMG_DIR, file_obj.name ])
	arch = open(ruta, 'w+b')
	for chunk in file_obj.chunks():
		arch.write(chunk)
	imagenVisita = ImagenVisita(visita=visita,foto=ruta)
	imagenVisita.save()
	return HttpResponse(len(file_obj))

@csrf_exempt
def obtenerImagenEspecie(request):
	especie = Especie.objects.get(id=request.GET.get("idEspecie"))
	return HttpResponse(especie.imagen)