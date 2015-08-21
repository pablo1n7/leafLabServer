#! /usr/bin/python
# -*- coding: UTF-8-*-

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.template import Variable, VariableDoesNotExist
import json
import socket
import ipdb
from models import *
import numpy as np

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
	puntos = Punto.objects.filter(visita = visita).order_by('orden')
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


def grillaTransecta(request):
	cantidadPuntos = 100;
	visita = Visita.objects.get(id = request.GET.get("idVisita"))
	puntos = Punto.objects.filter(visita = visita).order_by('orden')
	diccionarioEspecie = {}
	columnaPuntos = ['']
	matriz = []
	nroPunto = 1
	estados={" Suelo Desnudo ":"sueloDesnudo", " Muerto en Pie ":"muertoEnPie"," Toque Directo ":"toqueDirecto"}
	columnaPuntos = [""]+map(lambda x: estados[x],puntos.values_list('estadoPunto', flat=True))
	columnaPuntos.append("toqueDirecto") # para la ultima columna
	puntosSueloDesnudo = []
	puntosMuertoEnPie = []
	for punto in puntos:
		#columnaPuntos.append(estados[punto.estadoPunto])
		if estados[punto.estadoPunto] != "toqueDirecto":
			if estados[punto.estadoPunto] == "sueloDesnudo":
				puntosSueloDesnudo.append("X")
				puntosMuertoEnPie.append("")
			else:
				puntosSueloDesnudo.append("")
				puntosMuertoEnPie.append("X")
		else:
			puntosSueloDesnudo.append("")
			puntosMuertoEnPie.append("")

		plantas = Planta.objects.filter(punto = punto,toques__range=(0,100))
		for planta in plantas:

			if estados[punto.estadoPunto] != "toqueDirecto":
				toques = '-1';
				
			else:
				toques = str(planta.toques)


			if diccionarioEspecie.has_key(planta.especie.nombre):
				indice = diccionarioEspecie[planta.especie.nombre]
				if matriz[indice][nroPunto][0] != "":
					toques = int(toques) + int(matriz[indice][nroPunto][0])
			else:
				indice = len(diccionarioEspecie)
				diccionarioEspecie[planta.especie.nombre]=indice
				arregloIntermedio = []
				for x in range(cantidadPuntos+2):
					arregloIntermedio.append(("",columnaPuntos[x]))
				arregloIntermedio[cantidadPuntos+1] = ("0","toqueDirecto")
				matriz.append(arregloIntermedio)

				matriz[indice][0]=(planta.especie,"")
			matriz[indice][nroPunto] = (toques,estados[punto.estadoPunto])
		nroPunto+=1
	puntosToqueDirecto = puntos.filter(estadoPunto=" Toque Directo ")
	cantidadPlantas = {}
	for punto in puntosToqueDirecto:
		plantasPunto = Planta.objects.filter(punto=punto)
		for plantaPunto in plantasPunto:
			if cantidadPlantas.has_key(plantaPunto.especie.nombre):
				cantidadPlantas[plantaPunto.especie.nombre] += 1
			else:
				cantidadPlantas[plantaPunto.especie.nombre] = 1
	for cEspecies in cantidadPlantas:
		#ipdb.set_trace()
		matriz[diccionarioEspecie[cEspecies]][cantidadPuntos+1] = (str(cantidadPlantas[cEspecies]),"toqueDirecto")


	ipdb.set_trace()

	response = render_to_response('views/matrizTransecta.html',{"visita":visita,"matriz":matriz,"cantPuntos":range(1,(cantidadPuntos+1)),"estadoPuntos":columnaPuntos,"puntosSueloDesnudo":puntosSueloDesnudo,"puntosMuertoEnPie":puntosMuertoEnPie},content_type="application/x-excel; charset=utf-8")
	
	
	response.__setitem__("Content-Disposition",'attachment; filename="transecta-'+visita.obtenerFecha()+'.xls"')

	return response


@csrf_exempt
def getInfoPlanta(request):
	planta = Planta.objects.get(id=request.GET.get('idPlanta'))
	especies = Especie.objects.all()
	arregloEspeciesFormateadas = map(lambda x: [str(x.id),str(x.id),str(x.nombre)],especies[1:])
	especiesFormateadas = json.dumps(arregloEspeciesFormateadas)
	patron = json.dumps(map(lambda x: [x.nombre],especies[1:]))
	patron = patron.replace(",","|")[1:-1]
	#ipdb.set_trace()
	return render_to_response('views/infoPlanta.html',{'planta':planta,'especies': especiesFormateadas,'patron':patron})

@csrf_exempt
def getInfoEjemplar(request):
	ejemplar = Ejemplar.objects.get(id=request.GET.get('idEjemplar'))
	return render_to_response('views/infoEjemplar.html',{'ejemplar':ejemplar})


@csrf_exempt
def modificarPlanta(request):
	planta = Planta.objects.get(id=request.POST.get("id"))
	especie = Especie.objects.get(nombre=request.POST.get("especie"))
	planta.especie = especie
	planta.toques = request.POST.get("toques")
	planta.estadoFenologico = request.POST.get("estadoFenologico")
	planta.save()
	return HttpResponse()

@csrf_exempt
def modificarEjemplar(request):
	ejemplar = Ejemplar.objects.get(id=request.POST.get("id"))
	valores = json.loads(request.POST.get("valores"))
	for val in valores:
		valor = Valor.objects.get(id=val["idValor"])
		if ejemplar == valor.ejemplar :
			valor.valor = val["valor"]
			valor.save()
	return HttpResponse()