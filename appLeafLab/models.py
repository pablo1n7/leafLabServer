#! /usr/bin/python
# -*- coding: UTF-8-*-

from django.db import models,IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import re,ipdb,base64,Image,json, datetime, os
import uuid
import base64
import random as r

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
        if(patron.match(self.nombre.encode('utf-8'))):
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
        if(patron.match(self.nombre.encode('utf-8'))):
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
        if(patron.match(self.nombre.encode('utf-8'))):
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
        if(patron.match(self.nombre.encode('utf-8'))):
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
        if(patron.match(self.nombre.encode('utf-8'))):
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


# {"id":e.get("id"),"id_servidor":e.get("id_servidor"),"nombre":e.get("nombre"),
# "familiaLocal":e.get("familia").get("id"),"familia":familiasDicc[e.get("familia").get("id")],
# "formaBiologica":e.get("formaBiologica").id,"tipoBiologico":e.get("tipoBiologico").id,"estadoDeConservacion":e.get("estadoDeConservacion").id,
# "distribucionGeografica":e.get("distribucionGeografica").id,"indiceDeCalidad":e.get("indiceDeCalidad"),
# "forrajera":e.get("forrajera")}


    @classmethod
    def obtenerElementos(self,datos):
        especies = []
        claves = []
        for especieJson in datos:
            resultado = self.objects.filter(nombre=especieJson['nombre'])
            if not resultado:
                try:
                    especie = self.objects.get(id=especieJson['id_servidor'])
                except ObjectDoesNotExist, e:

                    especie = Especie(nombre=especieJson['nombre'])
                    especie.familia = Familia.objects.get(id=especieJson['familia'])
                    especie.formaBiologica = FormaBiologica.objects.get(id=especieJson['formaBiologica'])
                    especie.tipoBiologico = TipoBiologico.objects.get(id=especieJson['tipoBiologico'])
                    especie.estadoDeConservacion = EstadoDeConservacion.objects.get(id=especieJson['estadoDeConservacion'])
                    especie.distribucionGeografica = DistribucionGeografica.objects.get(id=especieJson['distribucionGeografica'])
                    especie.indiceDeCalidad = especieJson["indiceDeCalidad"]
                    especie.forrajera = especieJson["forrajera"]
                    especie.salvar()
            else:
                especie = resultado[0]
            
            especieJson["id_servidor"] = especie.id
            especieJson["nombre"] = especie.nombre
            especieJson["imagen"] = especie.imagen
            especies.append(especieJson)
            claves.append(especieJson["id_servidor"])

        especiesCompletas = filter(lambda x: x.id not in claves, self.objects.all())
        diccionarioDatos = map(lambda x:{"id_servidor":x.id,"nombre":x.nombre,"familia":x.familia.id,"formaBiologica":x.formaBiologica.id,"tipoBiologico":x.tipoBiologico.id,"estadoDeConservacion":x.estadoDeConservacion.id,"distribucionGeografica":x.distribucionGeografica.id,"indiceDeCalidad":x.indiceDeCalidad,"forrajera":x.forrajera,"imagen":x.imagen},especiesCompletas)
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
        imagen = datos["imagen"]
        if imagen != "":
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
            import cStringIO
            imgBuffer = cStringIO.StringIO()
            imagen.save(imgBuffer, format="JPEG")
            imgStr = base64.b64encode(imgBuffer.getvalue())
            self.imagen = imgStr
            os.remove('/'.join([settings.TEMP_DIR, self.nombre+'.png' ]))
        

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
        if(patron.match(self.nombre.encode('utf-8'))):
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
        if(patron.match(self.nombre.encode('utf-8'))):
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
#         t.executeSql('CREATE TABLE IF NOT EXISTS TipoPropiedad(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, idRango INTEGER,idEnumerado INTEGER, FOREIGN KEY (idRango) REFERENCES Rango(id),FOREIGN KEY (idEnumerado) REFERENCES Enumerado(id));', [], null, null);
#   });



class TipoPropiedad(models.Model):
    nombre = models.CharField(max_length=200)
    def representacion(self,valor):
        if self.id == 1:
            return "<div valor='"+str(valor.id)+"'><input placeholder='a,b,cd...' type='text' value='"+str(valor.valor)+"' /> </div>"
        
        if self.id ==2:
            return "<div valor='"+str(valor.id)+"'><input placeholder='0,1,2...' patron= '^(-?[0-9]+)$' value='"+str(valor.valor)+"' mensaje= '' type='number' /> </div>"
	
# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Enumerado(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, valores TEXT NOT NULL);', [], null, null);
# 	});



class Enumerado(TipoPropiedad):
    valores = models.CharField(max_length=200)
    def representacion(self,valor):
        elementoDom = "<div valor='"+str(valor.id)+"'><select name='enumerado'>"
        opciones = self.valores.split(",")
        for opcion in opciones:
            if str(valor.valor) == opcion:
                elementoDom = elementoDom+"<option selected>"+opcion+"</option>"
            else:
                elementoDom = elementoDom+"<option>"+opcion+"</option>" 
        elementoDom = elementoDom + "</select> </div>"
        return elementoDom

# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Rango(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, valorMin INTEGER NOT NULL, valorMax INTEGER NOT NULL);', [], null, null);
# 	});


class Rango(TipoPropiedad):
    valorMin = models.IntegerField()
    valorMax = models.IntegerField()

    def representacion(self,valor):
        identificador = r.randint(1,1000000)
        funcionChange = '$("#label'+identificador+'").text(this.value);'
        elementoDom = "<div valor='"+str(valor.id)+"'><input id='rango"+identificador+"' class='slider' onchange='"+funcionChange+"' type='range' min='"+self.valorMin+"' max='"+self.valorMax+"' value='"+str(valor.valor)+"'/>"
        labelRango = '<span id="label'+identificador+'" class="range-value"></span> </div>'
        elementoDom = elementoDom + labelRango
        return elementoDom

    # def representacion(self):
    #     pass


class Alfanumerico(TipoPropiedad):
	pass

class Nuemrico(TipoPropiedad):
	pass

# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Propiedad(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT NOT NULL, idTipoPropiedad INTEGER NOT NULL, FOREIGN KEY (idTipoPropiedad) REFERENCES TipoPropiedad(id));', [], null, null);
# 	});


tiposPropiedades = {"simple":lambda x:(TipoPropiedad.objects.get(id=x["idPadre"])),"rango":lambda x:(Rango(id=x["id"],valorMax=x["valorMax"],valorMin=x["valorMin"])),"enumerado":lambda x:(Enumerado(id=x["id"],valores=str(x["valores"]).replace("'","").replace("[","").replace("]","")
))}


class Propiedad(models.Model):
    tipoPropiedad = models.ForeignKey(TipoPropiedad,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    @classmethod
    def obtenerElementos(self,datos):
        
        propiedad = Propiedad(nombre=datos['nombre'],descripcion=datos["descripcion"])
        tipoPropiedad = tiposPropiedades[datos['tiposPropiedad']['tipo']](datos['tiposPropiedad'])
        tipoPropiedad.save()
        propiedad.tipoPropiedad = tipoPropiedad
        #ipdb.set_trace()
        propiedad.save()
        datos["id_servidor"] = propiedad.id
        datos["tiposPropiedad"]["id_servidor"] = tipoPropiedad.id
        return json.dumps(datos)

    def representacion(self,valor):
        div = "<div class='propiedadEjemplar'>"
        div = div + self.nombre
        div = div + self.tipoPropiedad.representacion(valor)
        div = div + "</div>"
        return div

    def __unicode__(self):
        return self.nombre


# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS TipoEjemplar(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,descripcion TEXT NOT NULL);', [], null, null);
# 	});

class TipoEjemplar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    propiedades = models.ManyToManyField(Propiedad)

    @classmethod
    def obtenerElementos(self,datos):
        tipoEjemplar = TipoEjemplar(nombre=datos["nombre"],descripcion=datos["descripcion"])
        tipoEjemplar.save()
        for campo in datos["campos"]:
            propiedad = Propiedad.objects.get(id=campo)
            tipoEjemplar.propiedades.add(propiedad)
        datos["id_servidor"] = tipoEjemplar.id
        return json.dumps(datos)

    def __unicode__(self):
        return self.nombre



# 	db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS TipoEjemplarPropiedad(idTipoEjemplar INTEGER NOT NULL, idPropiedad INTEGER NOT NULL, FOREIGN KEY (idTipoEjemplar) REFERENCES TipoEjemplar(id),FOREIGN KEY (idPropiedad) REFERENCES Propiedad(id),PRIMARY KEY(idTipoEjemplar,idPropiedad));', [], null, null);
# 	});



#    db.transaction(function (t) {
#        t.executeSql('CREATE TABLE IF NOT EXISTS Campania(nombre TEXT NOT NULL,descripcion TEXT, fecha INT NOT NULL, PRIMARY KEY(nombre,fecha));', [], null, null);
#    });

class Campania(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.BigIntegerField()
    descripcion = models.CharField(max_length=200)
    tiposEjemplares = models.ManyToManyField(TipoEjemplar)
    class Meta:
        unique_together = ("nombre", "fecha")

    def obtenerDescripcion(self):
        if self.descripcion == "":
            return "Sin Descripción"
        return self.descripcion

    def cantidadPlantasDesconocidas(self):
        tranectas = Transecta.objects.filter(campania = self)
        visitas = Visita.objects.filter(transecta = tranectas)
        especieDesconocida = Especie.objects.filter(nombre="No Definido")
        plantas = Planta.objects.filter(especie=especieDesconocida,visita=visitas,punto__isnull=False)
        return str(plantas.count())


    def obtenerFecha(self):
        fecha = datetime.datetime.fromtimestamp(self.fecha/1000)
        return fecha.strftime('%d/%m/%Y %H:%M')

    def obtenerCantidadTransectas(self):
        return len(Transecta.objects.filter(campania=self))

    @classmethod
    def obtenerElementos(self,datos):
        campania = Campania(nombre=datos["nombre"],descripcion=datos["descripcion"],fecha=datos["fecha"])
        campania.save()
        for idTipoEjemplar in datos["tiposEjemplaresAsociados"]:
            tipoEjemplar = TipoEjemplar.objects.get(id=idTipoEjemplar)
            campania.tiposEjemplares.add(tipoEjemplar)
        #ipdb.set_trace()
        datos["id_servidor"] = campania.id
        return json.dumps(datos)

    def __unicode__(self):
        return self.nombre

#     db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS Transecta(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nombreCampania TEXT NOT NULL,cuadro TEXT,fechaCampania INT NOT NULL,sentido FLOAT NOT NULL,ambiente TEXT NOT NULL,distanciaEntrePuntos INT NOT NULL, FOREIGN KEY (nombreCampania) REFERENCES Campania(nombre),FOREIGN KEY (fechaCampania) REFERENCES Campania(fecha));', [], null, null);
#     });

class Transecta(models.Model):
    cuadro = models.CharField(max_length=200, null=True)
    sentido = models.FloatField()
    ambiente = models.CharField(max_length=200)
    distanciaEntrePuntos = models.IntegerField(default=3)
    campania = models.ForeignKey(Campania, on_delete=models.PROTECT)

    def obtenerCuadro(self):
        if self.cuadro == "":
            return "Información de cuadro no proporcionada"
        return self.cuadro

    def obtenerSentido(self):
        return int(self.sentido)

    def cantidadPlantasDesconocidas(self):
        visitas = Visita.objects.filter(transecta = self)
        especieDesconocida = Especie.objects.filter(nombre="No Definido")
        plantas = Planta.objects.filter(especie=especieDesconocida,visita=visitas,punto__isnull=False)
        return str(plantas.count())

    def obtenerSentidoStr(self):
        sentido = self.obtenerSentido
        if sentido > 315 or sentido < 45:
            return "S-->N"
        if sentido > 45 and sentido < 135:
            return "O-->E"
        if sentido > 135 and sentido < 225:
            return "N-->S"
        
        return "E-->O"


    def obtenerCantidadVisitas(self):
        return len(Visita.objects.filter(transecta=self))

    def obtenerCoordenadas(self):
        try:
            visita = Visita.objects.filter(transecta=self)[0]
            puntos = Punto.objects.filter(visita=visita).order_by('orden')
            coordenadas = puntos[0].coordenada+","+puntos.reverse()[0].coordenada
        except Exception, e:
            coordenadas = "0,0"
        return coordenadas

    def obtenerCoordenadasGrados(self):
        strPos =""
        posiciones = self.obtenerCoordenadas().split(',')
        primeraPosicion = posiciones[0].split("/")
        ultimaPosicion  = posiciones[1].split("/")

        latPrimeraPosicion = float(primeraPosicion[0])
        lngPrimeraPosicion = float(primeraPosicion[1])

        deg = int(latPrimeraPosicion)
        auxMnt = (latPrimeraPosicion - deg)*60
        mnt = int( auxMnt)
        sec = (auxMnt - mnt) * 60
        strPos = strPos+str(deg)+"°"+str(abs(mnt))+"'"+str(abs(sec))+'"' +"/"

        deg = int(lngPrimeraPosicion)
        auxMnt = (lngPrimeraPosicion - deg)*60
        mnt = int( auxMnt)
        sec = (auxMnt - mnt) * 60
        strPos = strPos+str(deg)+"°"+str(abs(mnt))+"'"+str(abs(sec))+'"'

        return strPos;


    @classmethod
    def obtenerElementos(self,datos):
        campania = Campania.objects.get(id=datos["campania"])
        transecta = Transecta(cuadro=datos["cuadro"],sentido=datos["sentido"],ambiente=datos["ambiente"],distanciaEntrePuntos=datos["distanciaEntrePuntos"],campania=campania)
        transecta.save()
        #ipdb.set_trace()
        datos["id_servidor"] = transecta.id
        return json.dumps(datos)


    def __unicode__(self):
        return self.ambiente


#     db.transaction(function (t) {
#         t.executeSql('CREATE TABLE IF NOT EXISTS Visita(idTransecta INTEGER NOT NULL ,fecha INT NOT NULL,FOREIGN KEY (idTransecta) REFERENCES Transecta(id), PRIMARY KEY (idTransecta,fecha));', [], null, null);
#     });

class Visita(models.Model):
    transecta = models.ForeignKey(Transecta,on_delete=models.PROTECT)
    fecha = models.BigIntegerField()
    class Meta:
        unique_together = ("transecta", "fecha")



    def cantidadPlantasDesconocidas(self):
        especieDesconocida = Especie.objects.filter(nombre="No Definido")
        plantas = Planta.objects.filter(especie=especieDesconocida,visita=self,punto__isnull=False)
        return str(plantas.count())


    def calcularEstadisticas(self):

        puntos = Punto.objects.filter(visita = visita)
        estadisticasEspecies={}
#{"co":0,"coti":0,"cof":0}
        for punto in puntos:
            plantas = Planta.objects.filter(visita = visita,punto=punto)
            especiesEnPunto = []
            for planta in plantas:
                if( not(estadisticasEspecies.hasKey(planta.especie)) ):
                    estadisticasEspecies[planta.especie] = {"co":0,"coti":0,"cof":0,"tf":0,"ie":planta.especie.indiceDeCalidad}
                if planta.toques > 0:
                    if(not(planta.especie in especiesEnPunto)):
                        especiesEnPunto.append(planta.especie)
                        estadisticasEspecies[planta.especie]["coti"] += 1
                        estadisticasEspecies[planta.especie]["co"] += 1
                        if(planta.especie.forrajera == 1):
                            estadisticasEspecies[planta.especie]["cof"] +=1
                        
                else:
                    if(not(planta.especie in especiesEnPunto)):
                        especiesEnPunto.append(planta.especie)
                        estadisticasEspecies[planta.especie]["coti"] +=1

#                 if planta.especie.forrajera == 1:
#                     estadisticasEspecies[planta.especie]["cof"] +=1
#                    estadisticasEspecies[planta.especie]["tf"] +=planta.toques
#                    estadisticasEspecies[planta.especie]["tf*ie"] +=planta.toques

    def obtenerFecha(self):
        fecha = datetime.datetime.fromtimestamp(self.fecha/1000)
        return fecha.strftime('%d/%m/%Y %H:%M')

    def obtenerCantidadImagenes(self):
        return len(ImagenVisita.objects.filter(visita=self))

    def obtenerImagenes(self):
        imagenes = ""
        for imagen in ImagenVisita.objects.filter(visita=self):
            imagenes = imagenes+(imagen.foto.replace("appLeafLab/",""))+","
        return imagenes

    def obtenerCantidadItemsAsociados(self):
        return len(Ejemplar.objects.filter(visita=self,punto=None))+len(Planta.objects.filter(visita=self,punto=None))

    @classmethod
    def obtenerElementos(self,datos):
        transecta = Transecta.objects.get(id=datos["transecta"])
        visita = Visita(fecha=datos["fecha"],transecta=transecta)
        visita.save()
        #ipdb.set_trace()
        datos["id_servidor"] = visita.id
        return json.dumps(datos)

    def guardarImagen(self,ruta):
        imagenVisita = ImagenVisita(visita=self,foto=ruta)
        imagenVisita.save()


    def __unicode__(self):
        return datetime.datetime.fromtimestamp(self.fecha/1000).__str__()

#   db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Punto(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, idTransecta INTEGER NOT NULL, fecha INT NOT NULL, coordenada TEXT, estadoPunto TEXT NOT NULL, tipoSuelo TEXT NOT NULL, FOREIGN KEY (tipoSuelo) REFERENCES TipoSuelo(nombre),FOREIGN KEY (idTransecta, fecha) REFERENCES Visita(idTransecta,fecha));', [], null, null);
#   });

class Punto(models.Model):
    visita = models.ForeignKey(Visita,on_delete=models.PROTECT)
    suelo = models.ForeignKey(TipoSuelo,on_delete=models.PROTECT)
    orden = models.IntegerField()
    coordenada = models.CharField(max_length=200)
    estadoPunto = models.CharField(max_length=200)

    def cantidadPlantasDesconocidas(self):
        especieDesconocida = Especie.objects.filter(nombre="No Definido")
        plantas = Planta.objects.filter(especie=especieDesconocida,punto=self)
        return str(plantas.count())

    @classmethod
    def obtenerElementos(self,datos):
        visita = Visita.objects.get(id=datos["visita"])
        suelo = TipoSuelo.objects.get(id=datos["suelo"])
        orden = datos["orden"]
        punto = Punto(visita=visita,suelo=suelo, coordenada=datos["coordenadas"],estadoPunto=datos["estado"],orden=orden)
        punto.save()
        datos["id_servidor"] = punto.id
        return json.dumps(datos)
        
    def __unicode__(self):
        return self.id.__str__()




#    db.transaction(function (t) {
#       t.executeSql('CREATE TABLE IF NOT EXISTS Planta(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,idTransecta INTEGER NOT NULL,fecha INT NOT NULL,idPunto INTEGER,nombreEspecie TEXT NOT NULL, estadoFenologico TEXT,toques INTEGER NOT NULL, foto TEXT, FOREIGN KEY (nombreEspecie) REFERENCES Especie(nombre),FOREIGN KEY(idTransecta,fecha) REFERENCES Visita(idTransecta,fecha),FOREIGN KEY (idPunto) REFERENCES Punto(id));', [], null, null);
#    });

class Planta(models.Model):
    visita = models.ForeignKey(Visita,on_delete=models.PROTECT,null=True)
    punto = models.ForeignKey(Punto,on_delete=models.PROTECT,null=True)
    especie = models.ForeignKey(Especie,on_delete=models.PROTECT)
    estadoFenologico = models.CharField(max_length=200)
    toques = models.IntegerField(default=0)
    foto = models.CharField(max_length=10000000,null=True)

    @classmethod
    def obtenerElementos(self,datos):
        punto = None
        visita = Visita.objects.get(id=datos["visita"]);
        especie = Especie.objects.get(id=datos["especie"]);
        if datos["punto"] != "null":
            punto = Punto.objects.get(id=datos["punto"]);

        planta = Planta(visita=visita,punto = punto,especie=especie,toques=datos["toques"],estadoFenologico=datos["estadoFenologico"])
        planta.save()
        datos["id_servidor"] = planta.id
        return json.dumps(datos)

    def guardarImagen(self,ruta):
        self.foto = ruta
        self.save()

    def obtenerFoto(self):
        if self.foto == None:
            return ""
        return self.foto.replace("appLeafLab/","")
        


    def __unicode__(self):
        return self.id.__str__()




#   db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Ejemplar(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,idTipoEjemplar INTEGER NOT NULL,idTransecta INTEGER NOT NULL, idPunto INTEGER,fecha INT NOT NULL, foto TEXT,FOREIGN KEY (idTipoEjemplar) REFERENCES TipoEjemplar(id),FOREIGN KEY (idPunto) REFERENCES Punto(id),FOREIGN KEY(idTransecta,fecha) REFERENCES Visita(idTransecta,fecha));', [], null, null);
#   });

class Ejemplar(models.Model):
    tipoEjemplar = models.ForeignKey(TipoEjemplar,on_delete=models.PROTECT)
    punto = models.ForeignKey(Punto,blank=True, null=True,on_delete=models.PROTECT)
    visita = models.ForeignKey(Visita,on_delete=models.PROTECT,null=True)
    foto = models.CharField(max_length=10000000,null=True)

    @classmethod
    def obtenerElementos(self,datos):
        # ipdb.set_trace()
        punto = None
        visita = Visita.objects.get(id=datos["visita"]);
        tipoEjemplar = TipoEjemplar.objects.get(id=datos["tipoEjemplar"]);
        if datos["punto"] != "null":
            punto = Punto.objects.get(id=datos["punto"]);

        ejemplar = Ejemplar(visita=visita,punto = punto,tipoEjemplar=tipoEjemplar)
        ejemplar.save()
        datos["id_servidor"] = ejemplar.id
        return json.dumps(datos)

    def guardarImagen(self,ruta):
        self.foto = ruta
        self.save()

    def obtenerFoto(self):
        if self.foto == None:
            return ""
        return self.foto.replace("appLeafLab/","")

    def representacion(self):
        valores = Valor.objects.filter(ejemplar=self)
        elementoDom = "<div>"
        for valor in valores:
            elementoDom =   elementoDom + valor.propiedad.representacion(valor)
        return elementoDom +"</div>"
        


    def __unicode__(self):
        return self.id.__str__()
#   valores = models.ManyToManyField(Valor)


#   db.transaction(function (t) {
#     t.executeSql('CREATE TABLE IF NOT EXISTS Valor(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, idPropiedad INTEGER NOT NULL, idEjemplar INTEGER NOT NULL, valor TEXT NOT NULL, FOREIGN KEY (idPropiedad) REFERENCES Propiedad(id),FOREIGN KEY (idEjemplar) REFERENCES Ejemplar(id));', [], null, null);
#   });

class Valor(models.Model):
    propiedad = models.ForeignKey(Propiedad,on_delete=models.PROTECT)
    ejemplar = models.ForeignKey(Ejemplar,on_delete=models.PROTECT)
    valor = models.CharField(max_length=200)

    @classmethod
    def obtenerElementos(self,datos):
        
        propiedad = Propiedad.objects.get(id=datos["propiedad"]);
        ejemplar = Ejemplar.objects.get(id=datos["ejemplar"]);
        valor =Valor(valor=datos["valor"],ejemplar=ejemplar,propiedad=propiedad)
        valor.save()
        datos["id_servidor"] = valor.id
        return json.dumps(datos)


    def __unicode__(self):
        return self.id.__str__()


# Imagenes asociadas a las visitas de una transecta
class ImagenVisita(models.Model):
    foto = models.CharField(max_length=10000000)
    visita = models.ForeignKey(Visita,on_delete=models.PROTECT)