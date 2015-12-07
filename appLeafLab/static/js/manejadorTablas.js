var ManejadorTablas = function() {

	var tablas = [];
	var cantidadDeFilas = 6;


	this.agregarTabla = function(nombreTabla,idTabla,callbackClicRow,callbackAgregar) {

		tablas[nombreTabla] = $(idTabla).DataTable( {"lengthChange": false,"pageLength": cantidadDeFilas,"language": {
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

		if (nombreTabla == "tablaEspecies") {
			tablas[nombreTabla].column(5).visible(false);
			if (screen.width < 1366) {
				tablas[nombreTabla].column(3).visible(false);
				tablas[nombreTabla].column(4).visible(false);
			};
		};
	}

	return{
        tablas:tablas,
        agregarTabla: agregarTabla
    }

}();