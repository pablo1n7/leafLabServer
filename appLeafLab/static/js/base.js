const CODIGO_ERROR = 500;
const CODIGO_EXITO = 200;
const COMPLEJO = 1;
const SIMPLE = 0;
const CANTIDAD_PUNTOS = 100;

var marcadores = [];

$(document).ready(function(){	
	var footer = $($(".mastfoot")[0]);
	var valorTop = screen.height * 0.82;
	footer.css({"top":valorTop+"px"});
});




function mostrarMensajeExito(mensaje){
	alertify.success('<i class="fa fa-check"></i>  '+mensaje);
}

function mostrarMensajeError(mensaje){
	alertify.error('<i class="fa fa-ban"></i>  '+mensaje);
}

function mostrarMensajeLog(mensaje){
	alertify.message('<i class="fa fa-warning"></i>  '+mensaje);
}

function mostrarMensajeConfirmacion(titulo,mensaje,enAceptar,enCancelar){

	alertify.confirm(titulo, mensaje, enAceptar, enCancelar);

}

function lanzarModal (id,titulo,contenido,funcionAceptar,funcionEliminar) {
	var $modalBody = $($(id+" .modal-body")[0]);
	var $modalHeader = $($(id+" .modal-title")[0]);
	var $botonAceptar = $($(id+" .btn-primary")[0]);
	var $botonEliminar = $($(id+" .btn-danger")[0]);
	$botonEliminar.unbind();
	$botonEliminar.addClass("oculto");
	$modalHeader.empty();
	$modalHeader.append(titulo);
	$modalBody.empty();
	$modalBody.append(contenido);
	$botonAceptar.unbind();
	$botonAceptar.click(funcionAceptar);
	if(funcionEliminar != null){
		$botonEliminar.removeClass("oculto");
		$botonEliminar.click(function(){
			funcionEliminar();
		});
	}
	$(id).modal("show");
	$($modalBody.find("input")[1]).focus();
}


function actualizarValor(rango){
	$(rango.nextElementSibling).text(rango.value);
}

function activarSugerencias(campos,div){

	for (var i = campos.length - 1; i >= 0; i--) {
		activarSugerencia(ManejadorTablas.tablas[campos[i].tabla].data(),div.find("[name|="+campos[i].nombre+"]")[0])
	};
}

function activarSugerencia(datos,input) {
	var patron = "chiromplocono12345";
	if (datos.length == 0) {
		$(input).attr("patron",patron);
		return;	
	};
	patron = datos[0][2];
	for (var i = datos.length - 1; i >= 1; i--) {
		datos[i]
		patron = patron+"|"+datos[i][2];
	};
	$(input).attr("patron",patron);
	var options = {
       script: "inicio",
       varname: "inicio",
       json: true,
       maxentries: 6,
       noresults: "Sin Resultados!",
  valores:datos,
       alwaysSuggest: false
   };
   var as = new AutoSuggest(input, options);
}

function validarCampos($campos){
	var $inputs = $campos.find("input");
	var resultadoValidacion = $inputs.filter(function(k,elemento){
		return !validarCampo(elemento);
	});
	if(resultadoValidacion.length == 0)
		return true;
	return false;
}

function validarCampo(campo){
	$campo = $(campo);
    var valor = $campo.val();
    var patron = $campo.attr("patron");
    var reg = new RegExp(patron,"i");
    if(valor.match(reg)==null){
        mostrarMensajeError($campo.attr("mensaje"));
        //$campo.addClass("errorValidacion");
        $campo.addClass("inputError");
            //$campo.parent()[0].insertBefore($("<p id='"+$campo.attr("name")+"error' class='mensajeError'>"+ $campo.attr("mensaje") +"</p>").get(0),$campo.get(0));
        return false;
    }
    //$campo.removeClass("errorValidacion");
    //$("#"+$campo.attr("name")+"error").remove();
    $campo.removeClass("inputError");
    $campo.focus();
    return true;
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
          center: new google.maps.LatLng(-43.575269293192584,-68.78507825366209),
          zoom: 8,
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
	var marcadoresTransecta = [];
	for (var i = 0; i < CANTIDAD_PUNTOS; i++) {
		var latLng = new google.maps.LatLng(latLngInicial.lat()+(i*deltaLat),latLngInicial.lng()+(i*deltaLng));
		var marker = new google.maps.Marker({
		  position: latLng,
		  map: map,
		  title: 'Punto #'+(i+1),
		  icon:"http://maps.google.com/mapfiles/ms/icons/green-dot.png"
		});
		marcadores.push(marker);
		marcadoresTransecta.push(marker);
	};
  	marcadores.push(transecta);
  	return marcadoresTransecta;
}

function centrarPunto (nroPunto) {
	if(ultimoMarcador !=null)
		ultimoMarcador.setAnimation(null);

	ultimoMarcador = marcadores[nroPunto]
	map.setCenter(ultimoMarcador.position);
	map.setZoom(18);
	ultimoMarcador.setAnimation(google.maps.Animation.BOUNCE);

}


function calcularCentroTransecta(coordenadas) {
	var coord1 = coordenadas.split(",")[0];
	var coord2 = coordenadas.split(",")[1];
	var coord1Lat = parseFloat(coord1.split("/")[1]);
	var coord2Lat = parseFloat(coord2.split("/")[1]);
	var coord1Long = parseFloat(coord1.split("/")[0]);
	var coord2Long = parseFloat(coord2.split("/")[0]);
	var lat = (coord1Lat + coord2Lat)/2;
	var lng = (coord1Long + coord2Long)/2;
	var myLatlng = new google.maps.LatLng(lat,lng);
	return myLatlng;
}

function centrarTransecta(coordenadas) {
	vaciarMapa();
	dibujarTransecta(coordenadas);
	centroTranseta = calcularCentroTransecta(coordenadas);
	map.setCenter(centroTranseta);
	map.setZoom(16);
	
}

function centrarCampania(arrCoordenadas){
	var coordenadaFinal = {"lat":0,"lng":0};
	for (var i = arrCoordenadas.length - 1; i >= 0; i--) {
		coordenadaFinal["lat"] += arrCoordenadas[i].lat();
		coordenadaFinal["lng"] += arrCoordenadas[i].lng();
	};

	var radio = arrCoordenadas.length * 9000;

	coordenadaFinal["lat"] = coordenadaFinal["lat"] / arrCoordenadas.length;
	coordenadaFinal["lng"] = coordenadaFinal["lng"] / arrCoordenadas.length;
	var centroCampania = new google.maps.LatLng(coordenadaFinal["lat"],coordenadaFinal["lng"]);
	return centroCampania;
	//map.setCenter(centroCampania);


}