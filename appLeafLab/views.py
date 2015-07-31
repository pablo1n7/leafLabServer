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
rutaBase = {'visita':settings.VISITA_DIR,'ejemplar':settings.ITEM_DIR+"/ejemplar",'planta':settings.ITEM_DIR+"/planta"}

def index(request):
	campanias = Campania.objects.all()
	return render_to_response('views/index.html',{'campanias':campanias})

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
		print "----------------------------------------"
		print request.POST
		print "----------------------------------------"
		usuario = request.POST.get("identidad")
		tipoElemento = request.POST.get("nombre")
		datos = json.loads(request.POST.get("datos"))
		return HttpResponse(elementosSimples[tipoElemento].obtenerElementos(datos))	


@csrf_exempt
def identidad(request):
	nombrePC = socket.gethostname()
	ipPC = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
	cantEspecies = Especie.objects.all().count()
	cantFamilias = Familia.objects.all().count()
	jsondata = json.dumps({'nombrePC': nombrePC,'ip':ipPC,'infoAdicional':{"especies":cantEspecies,"familias":cantFamilias}})
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
	
#	visita = Visita.objects.get(id=request.POST.get('visita'))
	tipoElemento = elementosSimples[request.POST.get("nombre").lower()]
	elemento = tipoElemento.objects.get(id=request.POST.get('id_servidor'))
	file_obj = request.FILES['imagen']
	carpeta = '/'.join([rutaBase[request.POST.get("nombre").lower()],request.POST.get('id_servidor')])
	if not os.path.exists(carpeta): 
		os.makedirs(carpeta)
	#ruta = '/'.join([rutaBase[request.POST.get("nombre").lower()],request.POST.get("identidad"),request.POST.get('id_servidor'),file_obj.name])
	ruta = carpeta+"/"+file_obj.name
	arch = open(ruta, 'w+b')
	for chunk in file_obj.chunks():
		arch.write(chunk)

	elemento.guardarImagen(ruta)
	return HttpResponse(len(file_obj))

@csrf_exempt
def obtenerImagenEspecie(request):
	especie = Especie.objects.get(id=request.GET.get("idEspecie"))
	return HttpResponse(especie.imagen)

@csrf_exempt
def obtenerTransectas(request):
	campania = Campania.objects.get(id = request.GET.get("idCampania"))
	transectas = Transecta.objects.filter(campania = campania)
	return render_to_response('views/tablaTransecta.html',{"transectas":transectas})


@csrf_exempt
def obtenerVisitas(request):
	transecta = Transecta.objects.get(id = request.GET.get("idTransecta"))
	visitas = Visita.objects.filter(transecta = transecta)
	return render_to_response('views/tablaVisita.html',{"visitas":visitas,"transecta":transecta})


@csrf_exempt
def obtenerPuntos(request):
	visita = Visita.objects.get(id = request.GET.get("idVisita"))
	puntos = Punto.objects.filter(visita = visita)
	return render_to_response('views/tablaPuntos.html',{"puntos":puntos,"visita":visita})

@csrf_exempt
def obtenerAdjuntosVisita(request):
	visita = Visita.objects.get(id = request.GET.get("idVisita"))
	plantas = Planta.objects.filter(visita = visita, punto = None)
	ejemplares = Ejemplar.objects.filter(visita = visita, punto = None)
	condicion = (plantas.count() ==0) & (ejemplares.count() == 0);
	return render_to_response('views/tablaAdjuntos.html',{"condicion":not condicion, "ejemplares":ejemplares,"plantas":plantas})

@csrf_exempt
def obtenerDetallePunto(request):
	punto = Punto.objects.get(id=request.GET.get("idPunto"))
	plantas = Planta.objects.filter(punto = punto)
	ejemplares = Ejemplar.objects.filter(punto = punto)
	condicion = (plantas.count() ==0) & (ejemplares.count() == 0);
	return render_to_response('views/detallePunto.html',{"punto":punto, "condicion":not condicion, "ejemplares":ejemplares,"plantas":plantas})
