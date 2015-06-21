from django.db.models.signals import post_syncdb
import models


def crearValoresIniciales(sender, **kwargs):
	argumentos = {"id":1,"nombre":"No Definido"}
	print models.FormaBiologica.objects.get_or_create(argumentos)
	print models.TipoBiologico.objects.get_or_create(argumentos)
	print models.DistribucionGeografica.objects.get_or_create(argumentos)
	print models.EstadoDeConservacion.objects.get_or_create(argumentos)
	print models.TipoSuelo.objects.get_or_create(argumentos)
	print models.Familia.objects.get_or_create(argumentos)


post_syncdb.connect(crearValoresIniciales, sender=models)