#! /usr/bin/python
# -*- coding: UTF-8-*-
from django.db.models.signals import post_syncdb
import models


def crearValoresIniciales(sender, **kwargs):
	argumentos = {"id":1,"nombre":"No Definido"}
	formaBiologica = models.FormaBiologica.objects.get_or_create(argumentos)[0]
	tipoBiologico = models.TipoBiologico.objects.get_or_create(argumentos)[0]
	distribucionGeografica = models.DistribucionGeografica.objects.get_or_create(argumentos)[0]
	estadoDeConservacion = models.EstadoDeConservacion.objects.get_or_create(argumentos)[0]
	models.TipoSuelo.objects.get_or_create(argumentos)
	familia = models.Familia.objects.get_or_create(argumentos)[0]
	tipoProp = models.TipoPropiedad.objects.get_or_create(id=1,nombre="Alfanumerico")[0]
	models.TipoPropiedad.objects.get_or_create(id=2,nombre="Numérico")
	propiedad =  models.Propiedad.objects.get_or_create(id=1,nombre="Nota",descripcion="Agregue aqui sus ideas",tipoPropiedad=tipoProp)[0]
	tipoEjemplar = models.TipoEjemplar.objects.get_or_create(id=1,nombre="Nota",descripcion="unaNota")[0]
	tipoEjemplar.propiedades.add(propiedad)

	especie = models.Especie.objects.get_or_create(id=1,nombre="No Definido",familia=familia,formaBiologica=formaBiologica,tipoBiologico=tipoBiologico,distribucionGeografica=distribucionGeografica,indiceDeCalidad=0,forrajera=0,estadoDeConservacion=estadoDeConservacion)


	print "Valores por defecto creados con exito!"



post_syncdb.connect(crearValoresIniciales, sender=models)