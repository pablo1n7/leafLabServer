var ultimoMarcador = null;
var enVisita = false;
var alto = 0;
var fondoImagen = "";

$("document").ready(function(){

	alto = screen.height/2.5;
	$(".contenedorFlexible").css({"max-height":alto+"px"});
	$(".informacionAsociada").css({"top":(alto+20)+"px"});

	verMapa();
	inicializarCampanias();
	$("#contenedorTransectas").animate({"width":"0%"});
	$("#listarCampanias").click(function(){
		$("#contenedorCampanias").animate({"width":"80%"});
		$("#contenedorTransectas").animate({"width":"0%"});
		$("#contenedorVisitas").animate({"width":"0%"});
		$("#contenedorPuntos").animate({"width":"0%"});
		$("#contenedorDetallePunto").animate({"width":"0%"});
		$('#puntoActivo').empty();
		$('#puntoActivo').unbind();
		$('#campaniaActiva').empty();
		$('#campaniaActiva').unbind();
		$('#transectaActiva').empty();
		$('#transectaActiva').unbind();
		$('#visitaActiva').empty();
		$('#visitaActiva').unbind();
		$("#infoVisita").animate({"width":"0%"},400,"swing",function() {
			$("#mapa").removeClass("otroIzquierda");
			$("#infoVisita").addClass("oculto");
			enVisita = false;
		});
		vaciarMapa();

	});
	$("#contenedorCampanias").perfectScrollbar();
	$("#contenedorTransectas").perfectScrollbar();
	$("#contenedorVisitas").perfectScrollbar();
	$("#contenedorPuntos").perfectScrollbar();
	//$("#contenedorAdjuntosVisita").perfectScrollbar();

});

var gestorImagenes = function($imagenes){
	this.indiceActual = 0;
	this.arregloImagenes = $imagenes;
	_this = this;
	this.actualizar = function(indice){
		if(_this.arregloImagenes.length == 0){
			setTimeout(function(){_this.actualizar(0);},3000);
			return;
		}
		var indiceActual = indice%(_this.arregloImagenes.length);
		if(_this.arregloImagenes.length == 1){
			setTimeout(function(){_this.actualizar(indice+1);},3000);
			return;
		}
		if(enVisita)
			setTimeout(function(){_this.actualizar(indice+1);},3000);

		for (var i = indiceActual; i >= 0; i--){
			$(_this.arregloImagenes[i]).css({"width":"100%"});
		};

		for (var i = indiceActual; i < _this.arregloImagenes.length; i++) {
			$(_this.arregloImagenes[i]).css({"width":"0%"});
		};
		$(_this.arregloImagenes[indiceActual]).animate({"width":"100%"},400,"swing",function() {
		});
	};
	_this.actualizar();
}
var cambiarImagen = new gestorImagenes([]);


function reubicarMapa() {
	// body...
	$("#infoVisita").animate({"width":"0%"},400,"swing",function() {
		$("#mapa").removeClass("otroIzquierda");
		$("#infoVisita").addClass("oculto");
		enVisita = false;
	});
}

function inicializarCampanias(){
	var campanias = $("#contenedorCampanias").find("a");
	campanias.map(function(k,e){
		$(e).click(function(){
			var id = $(e).attr("id").split("-")[1];
			var nombre = $(e).find("h4").text();
			activarCampania(id)
		});
	});

}

function inicializarTransectas(){
	var transectas = $("#contenedorTransectas").find("a");
	transectas.map(function(k,e){
		$(e).click(function(){
			var id = $(e).attr("id").split("-")[1];
			var ambiente = $(e).find("h4").text();
			activarTransecta(id)
		});
	});
}

function inicializarVisitas(){
	var visitas = $("#contenedorVisitas").find("a");
	visitas.map(function(k,e){
		$(e).click(function(){
			var id = $(e).attr("id").split("-")[1];
			//var ambiente = $(e).find("h4").text();
			activarVisita(id)
		});
	});
}

function inicializarPuntos(){
	var puntos = $("#contenedorPuntos").find("a");
	puntos.map(function(k,e){
		$(e).click(function(){
			var id = $(e).attr("id").split("-")[1];
			activarPunto(id);
			centrarPunto(k);
		});
		$(e).hover(function(){
			centrarPunto(k);
		});
	});
}

function inicializarDetallePunto(){
	$("#imagenPunto").css({"height":$("#imagenPunto").width()})
	var adjuntos = $("#cuerpoDetallePunto").find("a");
	adjuntos.map(function(k,e){
		$(e).hover(function(){
			var imagen = $(e).attr("foto");
			if(imagen != ""){
				$("#imagenPunto").css({"background-image":"url('"+imagen+"')"});
				//$("#imagenPunto").css({"margin-top":"0px"});
				
			}
		},function(){
			$("#imagenPunto").css({"background-image":"url('"+fondoImagen+"')"});
				//$("#imagenPunto").css({"margin-top":"-25%"});
		});
	});
}



function cambiarEstadoNavegacion(elemento,idElemento) {
	switch(elemento){
		case "Campania":
			$(".itemNavegacion").empty();
			$('#campaniaActiva').append('/Campaña '+idElemento);
			$('#campaniaActiva').unbind();
			$('#campaniaActiva').click(function(){
				activarCampania(idElemento);
			});
			$("#contenedorVisitas").animate({"width":"0%"});
			$("#contenedorPuntos").animate({"width":"0%"});
			$("#contenedorDetallePunto").animate({"width":"0%"});
			reubicarMapa();
			break;
		
		case "Transecta":
			$(".itemNavegacion").map(function(k,e) {
				if (k >= 1) {
					$(e).empty();
				};
			});
			$("#transectaActiva").append("/Transecta "+idElemento);
			$('#transectaActiva').unbind();
			$('#transectaActiva').click(function(){
				activarTransecta(idElemento);
			});
			$("#contenedorPuntos").animate({"width":"0%"});
			$("#contenedorDetallePunto").animate({"width":"0%"});
			reubicarMapa();
			break;
		
		case "Visita":
			$(".itemNavegacion").map(function(k,e) {
				if (k >= 2) {
					$(e).empty();
				};
			});
			$("#visitaActiva").append("/Visita "+idElemento);
			$('#visitaActiva').unbind();
			$('#visitaActiva').click(function(){
				activarVisita(idElemento);
			});
			$("#contenedorDetallePunto").animate({"width":"0%"});
			break;
		
		case "Punto":
			$("#puntoActivo").empty().append("/Punto "+idElemento);
			$('#puntoActivo').unbind();
			$('#puntoActivo').click(function(){
				activarPunto(idElemento);
			});
			break;
			
	}
}


function activarCampania(idCampania){
	
	$.ajax({
	  url: "/obtenerTransectas",
	  data: { idCampania: idCampania}
	}).done(function(data) {
		cambiarEstadoNavegacion("Campania",idCampania);
		$("#contenedorTransectas").empty().append(data).animate({"width":"80%"});
		$("#contenedorCampanias").animate({"width":"0%"});
		inicializarTransectas();
	}).fail(function() {

	});

}

function activarTransecta(idTransecta){
	$.ajax({
	  url: "/obtenerVisitas",
	  data: { idTransecta: idTransecta}
	}).done(function(data){
		cambiarEstadoNavegacion("Transecta",idTransecta);	
		$("#contenedorVisitas").empty().append(data).animate({"width":"80%"});
		$("#contenedorTransectas").animate({"width":"0%"});		
		inicializarVisitas();
	}).fail(function() {

	});	


}

function activarVisita(idVisita){

	$.ajax({
	  url: "/obtenerPuntos",
	  data: { idVisita: idVisita}
	}).done(function(data) {
		cambiarEstadoNavegacion("Visita",idVisita);
		$("#contenedorPuntos").empty();
		$("#contenedorPuntos").append(data).animate({"width":"80%"});
		$("#contenedorVisitas").animate({"width":"0%"});
		$("#infoVisita").addClass("contenedorInformacionVisita");
		$("#mapa").addClass("otroIzquierda");
		$("#mapa").animate({"left":"0px"});
		$("#infoVisita").removeClass("oculto");
		inicializarPuntos();
		enVisita = true;
		$("#infoVisita").animate({"width":"48%"});
	}).fail(function() {

	});
	$.ajax({
	  url: "/obtenerAdjuntosVisita",
	  data: { idVisita: idVisita}
	}).done(function(data) {
		$("#contenedorAdjuntosVisita").css({"width":"68%"});
		$("#contenedorAdjuntosVisita").empty().append(data);
	}).fail(function() {

	});
	
}

function activarPunto(idPunto) {
	$.ajax({
	  url: "/obtenerDetallePunto",
	  data: { idPunto: idPunto}
	}).done(function(data) {
		cambiarEstadoNavegacion("Punto",idPunto);
		$("#contenedorDetallePunto").empty();
		$("#contenedorDetallePunto").append(data).animate({"width":"80%"},400,"swing",function(){
			inicializarDetallePunto();
		});
		$("#contenedorPuntos").animate({"width":"0%"});
	}).fail(function() {

	});
}



function cargarImagenesVisita(listaImagenes){
	arregloImagenes = [];
	console.log(listaImagenes);
	var imagenes = listaImagenes.split(",");
	var $contenedorImagenes = $('#contenedorImagenes');
	$contenedorImagenes.empty();
	$contenedorImagenes.css({"background-image":''});
	if(imagenes.length == 1){
		$("#contenedorAdjuntosVisita").css({"width":"100%"});
		return;
	}

	// var imagenBase = new Image();
	// imagenBase.src = imagenes[0];
	// if (imagenBase.width > imagenBase.height) {
	// 	$contenedorImagenes.css({"transform":"rotate(90deg)"});
	// }; 



	$("#contenedorImagenes").remove();
	//var $contenedorImagenes = $('<div id="contenedorImagenes" class="contenedorImagenes"></div>');
	$contenedorImagenes.css({"background-image":'url("'+imagenes[imagenes.length-2]+'")'});
	var $divAux = $('<div class="imagenVisita"/>');
	$divAux.css({"top":(alto+20)+"px"});
	$divAux.css({"background-image":'url("'+imagenes[0]+'")'});
	arregloImagenes.push($divAux);
	$contenedorImagenes.append($divAux);
	imagenes.map(function(e,k){
		if(e!="" && k != 0){
			var $div = $('<div class="imagenVisita"/>');
			$div.css({"top":(alto+20)+"px"})
			$div.css({"background-image":'url("'+e+'")'});
			arregloImagenes.push($div);
			$divAux.append($div);
			$divAux = $div;
		}
	});

	$('#infoVisita').append($contenedorImagenes);
	enVisita = true;
//	cambiarImagen(0);
	cambiarImagen.arregloImagenes = $($contenedorImagenes.find("div"));
}


// function cambiarImagen(indice){
// 	var indiceActual = indice%(arregloImagenes.length);
// 	if(arregloImagenes.length == 1)
// 		return;
// 	if(enVisita)
// 		setTimeout(function(){cambiarImagen(indice+1);},3000);

// 	for (var i = indiceActual; i >= 0; i--){
// 		arregloImagenes[i].css({"width":"100%"});
// 	};

// 	for (var i = indiceActual; i < arregloImagenes.length; i++) {
// 		arregloImagenes[i].css({"width":"0%"});
// 	};
// 	arregloImagenes[indiceActual].animate({"width":"100%"},400,"swing",function() {
// 	});
// }

function inicializarModalPlanta(idPlanta){
	$.get( "getInfoPlanta", { "idPlanta": idPlanta } )
	.done(function(data){
		lanzarModal("#modalModificarItem","Planta",data,modificarPlanta);
	});
}

function inicializarModalEjemplar(idEjemplar){

	$.get( "getInfoEjemplar", { "idEjemplar": idEjemplar } )
	.done(function(data){
		lanzarModal("#modalModificarItem","Ejemplar",data,modificarEjemplar);
	});
}

function modificarEjemplar(){
	console.log("enviar Datos Ejemplar");
	if ( validarCampos($("#item"))) {
		valoresNuevos = [];
		var valores = $("#item").find("input");
		$(valores).each(function(i,e){
			var idValor = $(e).parent().attr("valor");
			var valor = $(e).val();
			valoresNuevos.push({'idValor':idValor,'valor':valor});
		});
		var inputOpciones = $("#item").find("select");
		$(inputOpciones).each(function(i,e){
			var idValor = $(e).parent().attr("valor");
			var valor = $(e).val();
			valoresNuevos.push({'idValor':idValor,'valor':valor});
		});
		var id = $("#datosItemId").val();
		datosEjemplar = {"id":id,"valores":JSON.stringify(valoresNuevos)}
		$.post( "/modificarEjemplar", datosEjemplar)
		.done(function(data){
			mostrarMensajeExito("Ejemplar Modificado con éxito");
			$("#modalModificarItem").modal("hide");
			
		});
		
	};
}

function modificarPlanta(){
	console.log("enviar Datos Ejemplar");
	if ( validarCampos($("#datosPlanta"))) {

		var valores = $("#datosPlanta").find("input");
		datosPlanta = {"id":valores[0].value,"especie":valores[1].value,"estadoFenologico":valores[2].value,"toques":valores[3].value}
		$.post( "/modificarPlanta", datosPlanta)
		.done(function(data){
			mostrarMensajeExito("Planta Modificada con éxito");
			$("#modalModificarItem").modal("hide");
			
		});
		
	};
}

function cancelarModal(){
	console.log("enviar Datos Planta");
}