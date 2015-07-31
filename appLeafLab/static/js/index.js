var ultimoMarcador = null;
var marcadores = [];
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
	$("#contenedorAdjuntosVisita").perfectScrollbar();

});

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



function verMapa() {
		var styles = [
		{
			stylers: [
				{ saturation: -100 },
				{ lightness: -26 },
				{gamma: 0.2}
			]
		}];

		 var styledMap = new google.maps.StyledMapType(styles,{name: "Styled Map"});



        var mapOptions = {
          center: new google.maps.LatLng(-43.253432, -65.310137),
          zoom: 12,
          mapTypeId: google.maps.MapTypeId.SATELLITE,
          disableDefaultUI: true
        };
        map = new google.maps.Map(document.getElementById("mapa"),mapOptions);
        map.mapTypes.set('map_style', styledMap);
		map.setMapTypeId('map_style');
}


function vaciarMapa() {
	for (var i = 0; i < marcadores.length; i++) {
		marcadores[i].setMap(null);
	};
	marcadores = []
	map.setZoom(14);
}

function dibujarTransecta(coordenadas){
	var coord1 = coordenadas.split(",")[0];
	var coord2 = coordenadas.split(",")[1];
	var latLngInicial = new google.maps.LatLng(parseFloat(coord1.split("/")[1]),parseFloat(coord1.split("/")[0]));
	var latLngFinal = new google.maps.LatLng(parseFloat(coord2.split("/")[1]),parseFloat(coord2.split("/")[0]));
	var transecta = new google.maps.Polyline({
	    path: [latLngInicial,latLngFinal],
	    geodesic: true,
	    strokeColor: 'limegreen',
	    strokeOpacity: 1.0,
	    strokeWeight: 2
  	});
  	transecta.setMap(map);
	var deltaLat = (latLngFinal.lat() - latLngInicial.lat()) / (CANTIDAD_PUNTOS-1);
	var deltaLng = (latLngFinal.lng() - latLngInicial.lng()) / (CANTIDAD_PUNTOS-1);
	for (var i = 0; i < CANTIDAD_PUNTOS; i++) {
		var latLng = new google.maps.LatLng(latLngInicial.lat()+(i*deltaLat),latLngInicial.lng()+(i*deltaLng));
		var marker = new google.maps.Marker({
		  position: latLng,
		  map: map,
		  title: 'Punto #'+(i+1),
		  icon:"http://maps.google.com/mapfiles/ms/icons/green-dot.png"
		});
		marcadores.push(marker);
	};
  	marcadores.push(transecta);
}

function centrarPunto (nroPunto) {
	if(ultimoMarcador !=null)
		ultimoMarcador.setAnimation(null);

	ultimoMarcador = marcadores[nroPunto]
	map.setCenter(ultimoMarcador.position);
	map.setZoom(18);
	ultimoMarcador.setAnimation(google.maps.Animation.BOUNCE);

}

function centrarTransecta(coordenadas) {
	vaciarMapa();
	dibujarTransecta(coordenadas);
	var coord1 = coordenadas.split(",")[0];
	var coord2 = coordenadas.split(",")[1];
	var coord1Lat = parseFloat(coord1.split("/")[1]);
	var coord2Lat = parseFloat(coord2.split("/")[1]);
	var coord1Long = parseFloat(coord1.split("/")[0]);
	var coord2Long = parseFloat(coord2.split("/")[0]);
	var lat = (coord1Lat + coord2Lat)/2;
	var lng = (coord1Long + coord2Long)/2;
	var myLatlng = new google.maps.LatLng(lat,lng);
	map.setCenter(myLatlng);
	map.setZoom(16);
}

function cargarImagenesVisita(listaImagenes){
	arregloImagenes = [];
	console.log(listaImagenes);
	var imagenes = listaImagenes.split(",");
	var $contenedorImagenes = $('#contenedorImagenes')
	$contenedorImagenes.empty();
	$contenedorImagenes.css({"background-image":''});
	if(imagenes.length == 1){
		$("#contenedorAdjuntosVisita").css({"width":"100%"});
		return;
	}
	$("#contenedorImagenes").remove();
	//var $contenedorImagenes = $('<div id="contenedorImagenes" class="contenedorImagenes"></div>');
	$contenedorImagenes.css({"background-image":'url("'+imagenes[imagenes.length-2]+'")'});
	var $divAux = $('<div class="imagenVisita"/>');
	$divAux.css({"top":(alto+20)+"px"})
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
	cambiarImagen(0);
}

function cambiarImagen(indice){
	var indiceActual = indice%(arregloImagenes.length);
	if(arregloImagenes.length == 1)
		return;
	if(enVisita)
		setTimeout(function(){cambiarImagen(indice+1)},3000);

	for (var i = indiceActual; i >= 0; i--){
		arregloImagenes[i].css({"width":"100%"});
	};

	for (var i = indiceActual; i < arregloImagenes.length; i++) {
		arregloImagenes[i].css({"width":"0%"});
	};

	arregloImagenes[indiceActual].animate({"width":"100%"},400,"swing",function() {
		
	});
}