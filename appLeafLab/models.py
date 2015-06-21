#! /usr/bin/python
# -*- coding: UTF-8-*-

from django.db import models,IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import re,ipdb,base64,Image,json
import uuid
import base64

# Create your models here.

# db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS Familia(nombre TEXT NOT NULL PRIMARY KEY);', [], null, null);
#     });

class Familia(models.Model):
    nombre = models.CharField(max_length=200,unique=True)

    @classmethod
    def obtenerElementos(self,datos):

        familias = []
        claves = []
        for familiaJson in datos:
            #try:
            #ipdb.set_trace()
                #familia = Familia.objects.get(id=familiaJson['id_servidor'])
            resultado = Familia.objects.filter(nombre=familiaJson['nombre'])
            if not resultado:
                try:
                    familia = Familia.objects.get(id=familiaJson['id_servidor'])
                except ObjectDoesNotExist, e:
                    familia = Familia(nombre=familiaJson['nombre'])
                    familia.salvar()
            else:
                familia = resultado[0]
            familiaJson["id_servidor"] = familia.id
            familiaJson["nombre"] = familia.nombre
            familias.append(familiaJson)
            claves.append(familiaJson["id_servidor"])

        familiasCompletas = filter(lambda x: x.id not in claves, self.objects.all())
        diccionarioDatos = map(lambda x:{"id_servidor":x.id,"nombre":x.nombre},familiasCompletas)
        diccionarioDatos += familias
        
        return json.dumps(diccionarioDatos)

    def eliminar(self):
        respuesta = {'codigo': "200",'mensaje':"Familia eliminada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
        try:
            self.delete()
            return respuesta
        except IntegrityError, e:
            respuesta = {'codigo': "500",'mensaje':"Imposible eliminar:Familia actualmente en uso.",'objeto':{'id':self.id,'nombre':self.nombre}}
        return respuesta

            

    def salvar(self):
        patron = re.compile('^([a-zñáéíóú]+)([a-zñáéíóú0-9 ]+)$',re.IGNORECASE)
        if(patron.match(self.nombre)):
            try:
                self.save()
                respuesta = {'codigo': "200",'mensaje':"Operación realizada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
                return respuesta
            except IntegrityError, e:
                respuesta = {'codigo': "500",'mensaje':"Imposible realizar operación: Nombre duplicado."}
                return respuesta
        else:
            raise Exception()
            
    def __unicode__(self):
        return self.nombre

#     db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS FormaBiologica(nombre TEXT NOT NULL PRIMARY KEY);', [], null, null);
#     });

class FormaBiologica(models.Model):
    nombre = models.CharField(max_length=200,unique=True)

    @classmethod
    def obtenerElementos(self):
        datos = self.objects.all()
        diccionarioDatos = map(lambda x:{"id":x.id,"nombre":x.nombre}, datos)
        return json.dumps(diccionarioDatos)

    def eliminar(self):
        respuesta = {'codigo': "200",'mensaje':"Forma Biológica eliminada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
        try:
            self.delete()
            return respuesta
        except IntegrityError, e:
            respuesta = {'codigo': "500",'mensaje':"Imposible eliminar:Forma actualmente en uso.",'objeto':{'id':self.id,'nombre':self.nombre}}
        return respuesta

            

    def salvar(self):
        patron = re.compile('^([a-zñáéíóú]+)([a-zñáéíóú0-9 ]+)$',re.IGNORECASE)
        if(patron.match(self.nombre)):
            try:
                self.save()
                respuesta = {'codigo': "200",'mensaje':"Operación realizada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
                return respuesta
            except IntegrityError, e:
                respuesta = {'codigo': "500",'mensaje':"Imposible realizar operación: Nombre duplicado."}
                return respuesta
        else:
    		raise Exception()
    		
    def __unicode__(self):
    	return self.nombre
    
#     db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS TipoBiologico(nombre TEXT NOT NULL PRIMARY KEY);', [], null, null);
#     });

class TipoBiologico(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    @classmethod
    def obtenerElementos(self):
        datos = self.objects.all()
        diccionarioDatos = map(lambda x:{"id":x.id,"nombre":x.nombre}, datos)
        return json.dumps(diccionarioDatos)

    def eliminar(self):
        respuesta = {'codigo': "200",'mensaje':"Tipo Biológico eliminada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
        try:
            self.delete()
            return respuesta
        except IntegrityError, e:
            respuesta = {'codigo': "500",'mensaje':"Imposible eliminar:Tipo actualmente en uso.",'objeto':{'id':self.id,'nombre':self.nombre}}
        return respuesta          

    def salvar(self):
        patron = re.compile('^([a-zñáéíóú]+)([a-zñáéíóú0-9 ]+)$',re.IGNORECASE)
        if(patron.match(self.nombre)):
            try:
                self.save()
                respuesta = {'codigo': "200",'mensaje':"Operación realizada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
                return respuesta
            except IntegrityError, e:
                respuesta = {'codigo': "500",'mensaje':"Imposible realizar operación: Nombre duplicado."}
                return respuesta
        else:
            raise Exception()
            
    def __unicode__(self):
        return self.nombre


#     db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS DistribucionGeografica(nombre TEXT NOT NULL PRIMARY KEY);', [], null, null);
#     });

class DistribucionGeografica(models.Model):
    nombre = models.CharField(max_length=200,unique=True)

    @classmethod
    def obtenerElementos(self):
        datos = self.objects.all()
        diccionarioDatos = map(lambda x:{"id":x.id,"nombre":x.nombre}, datos)
        return json.dumps(diccionarioDatos)

    def eliminar(self):
        respuesta = {'codigo': "200",'mensaje':"Distribución Geográfica eliminada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
        try:
            self.delete()
            return respuesta
        except IntegrityError, e:
            respuesta = {'codigo': "500",'mensaje':"Imposible eliminar:Distribución Geográfica actualmente en uso.",'objeto':{'id':self.id,'nombre':self.nombre}}
        return respuesta

            

    def salvar(self):
        patron = re.compile('^([a-zñáéíóú]+)([a-zñáéíóú0-9 ]+)$',re.IGNORECASE)
        if(patron.match(self.nombre)):
            try:
                self.save()
                respuesta = {'codigo': "200",'mensaje':"Operación realizada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
                return respuesta
            except IntegrityError, e:
                respuesta = {'codigo': "500",'mensaje':"Imposible realizar operación: Nombre duplicado."}
                return respuesta
        else:
            raise Exception()
            
    def __unicode__(self):
        return self.nombre

#     db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS EstadoDeConservacion(nombre TEXT NOT NULL PRIMARY KEY);', [], null, null);
#     });

class EstadoDeConservacion(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    @classmethod
    def obtenerElementos(self):
        datos = self.objects.all()
        diccionarioDatos = map(lambda x:{"id":x.id,"nombre":x.nombre}, datos)
        return json.dumps(diccionarioDatos)

    def eliminar(self):
        respuesta = {'codigo': "200",'mensaje':"Estado de Conservación eliminado con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
        try:
            self.delete()
            return respuesta
        except IntegrityError, e:
            respuesta = {'codigo': "500",'mensaje':"Imposible eliminar:Estado actualmente en uso.",'objeto':{'id':self.id,'nombre':self.nombre}}
        return respuesta

            

    def salvar(self):
        patron = re.compile('^([a-zñáéíóú]+)([a-zñáéíóú0-9 ]+)$',re.IGNORECASE)
        if(patron.match(self.nombre)):
            try:
                self.save()
                respuesta = {'codigo': "200",'mensaje':"Operación realizada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
                return respuesta
            except IntegrityError, e:
                respuesta = {'codigo': "500",'mensaje':"Imposible realizar operación: Nombre duplicado."}
                return respuesta
        else:
            raise Exception()
            
    def __unicode__(self):
        return self.nombre

# 	 db.transaction(function (t) {
#        t.executeSql('CREATE TABLE IF NOT EXISTS Campania(nombre TEXT NOT NULL,descripcion TEXT, fecha INT NOT NULL, PRIMARY KEY(nombre,fecha));', [], null, null);
#    });

class Campania(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    class Meta:
		unique_together = ("nombre", "fecha")

#	  db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS Transecta(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nombreCampania TEXT NOT NULL,cuadro TEXT,fechaCampania INT NOT NULL,sentido FLOAT NOT NULL,ambiente TEXT NOT NULL,distanciaEntrePuntos INT NOT NULL, FOREIGN KEY (nombreCampania) REFERENCES Campania(nombre),FOREIGN KEY (fechaCampania) REFERENCES Campania(fecha));', [], null, null);
#     });

class Transecta(models.Model):
	cuadro = models.CharField(max_length=200)
	sentido = models.FloatField()
	ambiente = models.CharField(max_length=200)
	distanciaEntrePuntos = models.IntegerField(default=3)
	campania = models.ForeignKey(Campania, on_delete=models.PROTECT)



# 	  db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS Visita(idTransecta INTEGER NOT NULL ,fecha INT NOT NULL,FOREIGN KEY (idTransecta) REFERENCES Transecta(id), PRIMARY KEY (idTransecta,fecha));', [], null, null);
#     });

class Visita(models.Model):
	transecta = models.ForeignKey(Transecta,on_delete=models.PROTECT)
	fecha = models.IntegerField()
	class Meta:
		unique_together = ("transecta", "fecha")



# 	  db.transaction(function (t) {
#        t.executeSql('CREATE TABLE IF NOT EXISTS Especie(familia TEXT NOT NULL, nombre TEXT NOT NULL PRIMARY KEY,formaBiologica TEXT NOT NULL, tipoBiologico TEXT NOT NULL , distribucionGeografica TEXT NOT NULL, indiceDeCalidad INTEGER NOT NULL, forrajera INT NOT NULL ,estadoDeConservacion TEXT NOT NULL,imagen TEXT, FOREIGN KEY (familia) REFERENCES Familia(nombre),FOREIGN KEY (formaBiologica) REFERENCES FormaBiologica(nombre),FOREIGN KEY (tipoBiologico) REFERENCES TipoBiologico(nombre),FOREIGN KEY (distribucionGeografica) REFERENCES DistribucionGeografica(nombre),FOREIGN KEY (estadoDeConservacion) REFERENCES EstadoDeConservacion(nombre));', [], null, null);
#    });

class Especie(models.Model):
    nombre = models.CharField(max_length=200, unique=True);
    familia = models.ForeignKey(Familia,on_delete=models.PROTECT)
    formaBiologica = models.ForeignKey(FormaBiologica,on_delete=models.PROTECT)
    tipoBiologico = models.ForeignKey(TipoBiologico,on_delete=models.PROTECT)
    distribucionGeografica = models.ForeignKey(DistribucionGeografica,on_delete=models.PROTECT)
    indiceDeCalidad = models.IntegerField()
    forrajera = models.IntegerField()
    estadoDeConservacion = models.ForeignKey(EstadoDeConservacion,on_delete=models.PROTECT)
    imagen = models.CharField(max_length=10000000)

    @classmethod
    def obtenerElementos(self,datos):
        ipdb.set_trace()
        especies = []
        claves = []
        for familiaJson in datos:
            #try:
            #ipdb.set_trace()
                #familia = Familia.objects.get(id=familiaJson['id_servidor'])
            resultado = Familia.objects.filter(nombre=familiaJson['nombre'])
            if not resultado:
                try:
                    familia = Familia.objects.get(id=familiaJson['id_servidor'])
                except ObjectDoesNotExist, e:
                    familia = Familia(nombre=familiaJson['nombre'])
                    familia.salvar()
            else:
                familia = resultado[0]
            familiaJson["id_servidor"] = familia.id
            familiaJson["nombre"] = familia.nombre
            especies.append(familiaJson)
            claves.append(familiaJson["id_servidor"])

        especiesCompletas = filter(lambda x: x.id not in claves, self.objects.all())
        diccionarioDatos = map(lambda x:{"id_servidor":x.id,"nombre":x.nombre},especiesCompletas)
        diccionarioDatos += especies
        
        return json.dumps(diccionarioDatos)

    def construir(self, datos):
        self.familia = Familia.objects.get(nombre=datos["familia"])
        self.formaBiologica = FormaBiologica.objects.get(nombre=datos["forma"])
        self.tipoBiologico = TipoBiologico.objects.get(nombre=datos["tipoBiologico"])
        self.distribucionGeografica = DistribucionGeografica.objects.get(nombre=datos["distribucion"])
        self.indiceDeCalidad = datos["indice"]
        self.estadoDeConservacion = EstadoDeConservacion.objects.get(nombre=datos["estado"])
        self.forrajera = datos["forrajera"]
        imagen = datos["imagen"];
        if imagen != "null":
            base64_image = str(imagen).split(',')[1]
            imgfile = open('/'.join([settings.TEMP_DIR, self.nombre+'.png' ]), 'w+b')
            imgfile.write(base64.decodestring(base64_image))
            imgfile.seek(0)
            f = Image.open(imgfile)
            ancho = int(float(datos["coodenadasImagen[ancho]"])*f.size[0])
            alto = int(float(datos["coodenadasImagen[alto]"])*f.size[1])
            x= int(float(datos["coodenadasImagen[x]"])*f.size[0])
            y= int(float(datos["coodenadasImagen[y]"])*f.size[1])
            imagen= f.crop((x,y,x+ancho,y+alto))
            imagen = imagen.resize((450, 450), Image.ANTIALIAS)
           
            ipdb.set_trace()
#            self.imagen = base64.b64encode(imagen.tostring())
           # self.imagen = imagen.tostring()



        

    def eliminar(self):
        respuesta = {'codigo': "200",'mensaje':"Especie eliminada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
        try:
            self.delete()
            return respuesta
        except IntegrityError, e:
            respuesta = {'codigo': "500",'mensaje':"Imposible eliminar:Estado actualmente en uso.",'objeto':{'id':self.id,'nombre':self.nombre}}
        return respuesta

            

    def salvar(self):
        patron = re.compile('^([a-zñáéíóú]+)([a-zñáéíóú0-9 ]+)$',re.IGNORECASE)
        if(patron.match(self.nombre)):
            try:
                self.save() 
                respuesta = {'codigo': "200",'mensaje':"Operación realizada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
                return respuesta
            except IntegrityError, e:
                respuesta = {'codigo': "500",'mensaje':"Imposible realizar operación: Nombre duplicado."}
                return respuesta
        else:
            raise Exception()
            
    def __unicode__(self):
        return self.nombre


#    db.transaction(function (t) {
#	 	t.executeSql('CREATE TABLE IF NOT EXISTS Planta(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,idTransecta INTEGER NOT NULL,fecha INT NOT NULL,idPunto INTEGER,nombreEspecie TEXT NOT NULL, estadoFenologico TEXT,toques INTEGER NOT NULL, foto TEXT, FOREIGN KEY (nombreEspecie) REFERENCES Especie(nombre),FOREIGN KEY(idTransecta,fecha) REFERENCES Visita(idTransecta,fecha),FOREIGN KEY (idPunto) REFERENCES Punto(id));', [], null, null);
#    });

class Planta(models.Model):
	visita = models.ForeignKey(Visita,on_delete=models.PROTECT)
	especie = models.ForeignKey(Especie,on_delete=models.PROTECT)
	estadoFenologico = models.CharField(max_length=200)
	toques = models.IntegerField(default=0)
	foto = models.CharField(max_length=100000)

# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS TipoSuelo(nombre TEXT NOT NULL, PRIMARY KEY (nombre));', [], null, null);
# 	});


class TipoSuelo(models.Model):
    nombre = models.CharField(max_length=200,unique=True)

    @classmethod
    def obtenerElementos(self):
        datos = self.objects.all()
        diccionarioDatos = map(lambda x:{"id":x.id,"nombre":x.nombre}, datos)
        return json.dumps(diccionarioDatos)

    def eliminar(self):
        respuesta = {'codigo': "200",'mensaje':"Tipo Suelo eliminado con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
        try:
            self.delete()
            return respuesta
        except IntegrityError, e:
            respuesta = {'codigo': "500",'mensaje':"Imposible eliminar:Tipo actualmente en uso.",'objeto':{'id':self.id,'nombre':self.nombre}}
        return respuesta

            

    def salvar(self):
        patron = re.compile('^([a-zñáéíóú]+)([a-zñáéíóú0-9 ]+)$',re.IGNORECASE)
        if(patron.match(self.nombre)):
            try:
                self.save()
                respuesta = {'codigo': "200",'mensaje':"Operación realizada con exito.",'objeto':{'id':self.id,'nombre':self.nombre}}
                return respuesta
            except IntegrityError, e:
                respuesta = {'codigo': "500",'mensaje':"Imposible realizar operación: Nombre duplicado."}
                return respuesta
        else:
            raise Exception()
            
    def __unicode__(self):
        return self.nombre


# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Punto(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, idTransecta INTEGER NOT NULL, fecha INT NOT NULL, coordenada TEXT, estadoPunto TEXT NOT NULL, tipoSuelo TEXT NOT NULL, FOREIGN KEY (tipoSuelo) REFERENCES TipoSuelo(nombre),FOREIGN KEY (idTransecta, fecha) REFERENCES Visita(idTransecta,fecha));', [], null, null);
# 	});

class Punto(models.Model):
	visita = models.ForeignKey(Visita,on_delete=models.PROTECT)
	suelo = models.ForeignKey(TipoSuelo,on_delete=models.PROTECT)
	coordenada = models.CharField(max_length=200)
	estadoPunto = models.CharField(max_length=200)


# 	db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS TipoPropiedad(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, idRango INTEGER,idEnumerado INTEGER, FOREIGN KEY (idRango) REFERENCES Rango(id),FOREIGN KEY (idEnumerado) REFERENCES Enumerado(id));', [], null, null);
#   });



class TipoPropiedad(models.Model):
	nombre = models.CharField(max_length=200)
	
# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Enumerado(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, valores TEXT NOT NULL);', [], null, null);
# 	});



class Enumerado(TipoPropiedad):
	valores = models.CharField(max_length=200)


# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Rango(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, valorMin INTEGER NOT NULL, valorMax INTEGER NOT NULL);', [], null, null);
# 	});


class Rango(TipoPropiedad):
	valorMin = models.IntegerField()
	valorMax = models.IntegerField()


class Alfanumerico(TipoPropiedad):
	pass

class Nuemrico(TipoPropiedad):
	pass

# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Propiedad(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT NOT NULL, idTipoPropiedad INTEGER NOT NULL, FOREIGN KEY (idTipoPropiedad) REFERENCES TipoPropiedad(id));', [], null, null);
# 	});


class Propiedad(models.Model):
	tipoPropiedad = models.ForeignKey(TipoPropiedad,on_delete=models.PROTECT)
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)


# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS TipoEjemplar(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,descripcion TEXT NOT NULL);', [], null, null);
# 	});

class TipoEjemplar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    propiedades = models.ManyToManyField(Propiedad)



# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Ejemplar(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,idTipoEjemplar INTEGER NOT NULL,idTransecta INTEGER NOT NULL, idPunto INTEGER,fecha INT NOT NULL, foto TEXT,FOREIGN KEY (idTipoEjemplar) REFERENCES TipoEjemplar(id),FOREIGN KEY (idPunto) REFERENCES Punto(id),FOREIGN KEY(idTransecta,fecha) REFERENCES Visita(idTransecta,fecha));', [], null, null);
# 	});

class Ejemplar(models.Model):
	tipoEjemplar = models.ForeignKey(TipoEjemplar,on_delete=models.PROTECT)
	transecta = models.ForeignKey(Transecta,blank=True, null=True,on_delete=models.PROTECT)
	punto = models.ForeignKey(Punto,blank=True, null=True,on_delete=models.PROTECT)
	foto = models.CharField(max_length=200)
#	valores = models.ManyToManyField(Valor)





# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS TipoEjemplarPropiedad(idTipoEjemplar INTEGER NOT NULL, idPropiedad INTEGER NOT NULL, FOREIGN KEY (idTipoEjemplar) REFERENCES TipoEjemplar(id),FOREIGN KEY (idPropiedad) REFERENCES Propiedad(id),PRIMARY KEY(idTipoEjemplar,idPropiedad));', [], null, null);
# 	});



# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Valor(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, idPropiedad INTEGER NOT NULL, idEjemplar INTEGER NOT NULL, valor TEXT NOT NULL, FOREIGN KEY (idPropiedad) REFERENCES Propiedad(id),FOREIGN KEY (idEjemplar) REFERENCES Ejemplar(id));', [], null, null);
# 	});

class Valor(models.Model):
	propiedad = models.ForeignKey(Propiedad,on_delete=models.PROTECT)
	ejemplar = models.ForeignKey(Ejemplar,on_delete=models.PROTECT)
	valor = models.CharField(max_length=200)