


/*
	
	tablaFormaBiologicas = $("#tablaFormaBiologica").DataTable( {"lengthChange": false,"pageLength": 7,"language": {
  "zeroRecords": "Busqueda sin resultados","emptyTable": "No hay Formas Biológicas que mostrar","search": "Buscar","info": "Mostrando Página _PAGE_ de _PAGES_","paginate": {
    "previous": "Anterior","next":"Siguiente"}
  }});

$('#tablaFormaBiologica tbody').on( 'click', 'tr', function () {
		tablaFormaBiologicas.$('tr.selected').removeClass('selected');
        $(this).addClass('selected');
        var nombre = $($(this).find("td")[2]).text();
        var id = $($(this).find("td")[1]).text();
        var $contenidoFormulario = clonar($("#modeloCargaFormaBiologica"),"datosFormaBiologica",{"nombre":nombre,"id":id});
		lanzarModal("#modalCarga","Editar Forma Biológica",$contenidoFormulario,enviarFormaBiologica,eliminarFormaBiologica);
    } );



var agregarForma = $('<div class="divBoton botonAgregar"><a><i class="fa fa-plus"></i> Agregar</a></div>');
agregarForma.click(function(){
		agregarFormaBiologica();
});
$("#tablaFormaBiologica_filter").before(agregarForma);



*/

var ManejadorTablas = function() {

	var tablas = [];

	this.agregarTabla = function(nombreTabla,idTabla,callbackClicRow,callbackAgregar) {

		tablas[nombreTabla] = $(idTabla).DataTable( {"lengthChange": false,"pageLength": 6,"language": {
  "zeroRecords": "Busqueda sin resultados","emptyTable": "No hay elementos que mostrar","search": "Buscar","info": "Mostrando Página _PAGE_ de _PAGES_","paginate": {
    "previous": "Anterior","next":"Siguiente"}
  }});

		$(idTabla+' tbody').on( 'click', 'tr', function () {
			if ($(this.children[0]).hasClass("dataTables_empty") ) {
				return;
			};
			tablas[nombreTabla].$('tr.selected').removeClass('selected');
	        $(this).addClass('selected');
	        callbackClicRow(this);

	    } );
	    var agregar = $('<div class="divBoton botonAgregar"><a><i class="fa fa-plus"></i> Agregar</a></div>');
		agregar.click(callbackAgregar);
		$(idTabla+"_filter").before(agregar);

		
	}

	return{
        tablas:tablas,
        agregarTabla: agregarTabla
    }

}();