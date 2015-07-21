"""leafLabServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from appLeafLab import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^campanias', views.campain,name="campain"),
    url(r'^estadisticas', views.statistics,name="statistics"),
    
    url(r'^baseDeDatos/altaElemento', views.altaElementoSimple,name="altaElemento"),
    url(r'^baseDeDatos/bajaElemento', views.bajaElementoSimple,name="bajaElemento"),
    
    url(r'^baseDeDatos', views.dataBase,name="dataBase"),
    url(r'^about', views.about,name="about"),

    url(r'^administracion', views.administracionDeDatos,name="administracionDeDatos"),
    url(r'^sinc', views.sincronizar,name="sincronizar"),
    url(r'^quienSos', views.identidad,name="identidad"),
    url(r'^subirImagen', views.subirImagenes,name="subirImagen"),
    url(r'^getImagenEspecie', views.obtenerImagenEspecie,name="getImagenEspecie"),
    url(r'^', views.index,name="index")
    

]
