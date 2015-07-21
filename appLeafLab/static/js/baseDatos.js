var camposAutocompletados =[{nombre:"estado",tabla:"tablaEstadosConservacion"},{nombre:"distribucion",tabla:"tablaDistribucionesGeograficas"},{nombre:"familia",tabla:"tablaFamilias"},{nombre:"forma",tabla:"tablaFormaBiologicas"},{nombre:"tipo",tabla:"tablaTipoBiologicos"}];
var seleccionado = "formaBiologica";
var anteriorSeleccionado = "formaBiologica";
$(document).ready(function() {

	/*Definicion de las tablas de datos*/

	ManejadorTablas.agregarTabla("tablaFormaBiologicas","#tablaFormaBiologica",function(row) {
			var nombre = $($(row).find("td")[2]).text();
	        var id = $($(row).find("td")[1]).text();
	        var $contenidoFormulario = clonar($("#modeloCargaFormaBiologica"),"datosFormaBiologica",{"nombre":nombre,"id":id});
			lanzarModal("#modalCarga","Editar Forma Biológica",$contenidoFormulario,function(){
				enviarElemento($("#datosFormaBiologica"));
			},function(){
				eliminarElemento($("#datosFormaBiologica"));
			});
	},function(){
		agregarElemento("#modeloCargaFormaBiologica","datosFormaBiologica","Nueva Forma Biológica");
	});

	ManejadorTablas.agregarTabla("tablaTipoBiologicos","#tablaTipoBiologico",function(row) {
			var nombre = $($(row).find("td")[2]).text();
	        var id = $($(row).find("td")[1]).text();
	        var $contenidoFormulario = clonar($("#modeloCargaTipoBiologico"),"datosTipoBiologico",{"nombre":nombre,"id":id});
			lanzarModal("#modalCarga","Editar Tipo Biológico",$contenidoFormulario,function(){
				enviarElemento($("#datosTipoBiologico"));
			},function(){
				eliminarElemento($("#datosTipoBiologico"));
			});
	},function(){
		agregarElemento("#modeloCargaTipoBiologico","datosTipoBiologico","Nuevo Tipo Biológico");
	});

	ManejadorTablas.agregarTabla("tablaEstadosConservacion","#tablaEstadosConservacion",function(row) {
			var nombre = $($(row).find("td")[2]).text();
	        var id = $($(row).find("td")[1]).text();
	        var $contenidoFormulario = clonar($("#modeloCargaEstadoConservacion"),"datosEstadoConservacion",{"nombre":nombre,"id":id});
			lanzarModal("#modalCarga","Editar Estado de Conservación",$contenidoFormulario,function(){
				enviarElemento($("#datosEstadoConservacion"));
			},function(){
				eliminarElemento($("#datosEstadoConservacion"));
			});
	},function(){
		agregarElemento("#modeloCargaEstadoConservacion","datosEstadoConservacion","Nuevo Estado de Conservación");
	});

	ManejadorTablas.agregarTabla("tablaFamilias","#tablaFamilias",function(row) {
			var nombre = $($(row).find("td")[2]).text();
	        var id = $($(row).find("td")[1]).text();
	        var $contenidoFormulario = clonar($("#modeloCargaFamilia"),"datosFamilia",{"nombre":nombre,"id":id});
			lanzarModal("#modalCarga","Editar Familia",$contenidoFormulario,function(){
				enviarElemento($("#datosFamilia"));
			},function(){
				eliminarElemento($("#datosFamilia"));
			});
	},function(){
		agregarElemento("#modeloCargaFamilia","datosFamilia","Nueva Familia");
	});

	ManejadorTablas.agregarTabla("tablaTiposSuelo","#tablaTiposSuelo",function(row) {
			var nombre = $($(row).find("td")[2]).text();
	        var id = $($(row).find("td")[1]).text();
	        var $contenidoFormulario = clonar($("#modeloCargaTipoSuelo"),"datosTipoSuelo",{"nombre":nombre,"id":id});
			lanzarModal("#modalCarga","Editar Tipo Suelo",$contenidoFormulario,function(){
				enviarElemento($("#datosTipoSuelo"));
			},function(){
				eliminarElemento($("#datosTipoSuelo"));
			});
	},function(){
		agregarElemento("#modeloCargaTipoSuelo","datosTipoSuelo","Nuevo Tipo Suelo");
	});

	ManejadorTablas.agregarTabla("tablaDistribucionesGeograficas","#tablaDistribucionesGeograficas",function(row) {
			var nombre = $($(row).find("td")[2]).text();
	        var id = $($(row).find("td")[1]).text();
	        var $contenidoFormulario = clonar($("#modeloCargaDistribucionGeografica"),"datosDistribucionGeografica",{"nombre":nombre,"id":id});
			lanzarModal("#modalCarga","Editar Distribución Geográfica",$contenidoFormulario,function(){
				enviarElemento($("#datosDistribucionGeografica"));
			},function(){
				eliminarElemento($("#datosDistribucionGeografica"));
			});
	},function(){
		agregarElemento("#modeloCargaDistribucionGeografica","datosDistribucionGeografica","Nueva Distribucion Geografica");
	});

	ManejadorTablas.agregarTabla("tablaEspecies","#tablaEspecies",function(row) {
			var nombre = $($(row).find("td")[2]).text();
	        var id = $($(row).find("td")[1]).text();
	        var forma = $($(row).find("td")[4]).text();
	        var tipoBiologico = $($(row).find("td")[5]).text();
	        var estado = $($(row).find("td")[9]).text();
	        var distribucion = $($(row).find("td")[6]).text();
	        var familia = $($(row).find("td")[3]).text();
	        var indice = $($(row).find("td")[7]).text();
	        var forrajera = $($(row).find("td")[8]).text();

	        

	       
	        var $contenidoFormulario = clonar($("#modeloCargaEspecie"),"datosEspecie",{"nombre":nombre,"id":id,"forma":forma,"tipo":tipoBiologico,"estado":estado,"distribucion":distribucion,"familia":familia,"indice":indice});
			lanzarModal("#modalCarga","Editar Especie",$contenidoFormulario,function(){
				enviarElemento($("#datosEspecie"),COMPLEJO);
			},function(){
				eliminarElemento($("#datosEspecie"));
			});
			$($("#datosEspecie").find("[name|=indice]")[0].nextElementSibling).text(indice);
			if (forrajera == 0) {
				$("#datosEspecie").find("[name|=forrajera]")[0].click();
			};
			activarSugerencias(camposAutocompletados,$("#datosEspecie"));
			ImagenCroop.inicializar("divDragNDrop","divContenedorImagen","imagen","botonCambiarImagen");
        	$.get( "getImagenEspecie", { "idEspecie": id } )
			  .done(function( data ) {

			  	if (data!="") {
			  		setTimeout(function(){
					    ImagenCroop.instanciarImagen("data:image/jpeg;base64,"+data);
					    ImagenCroop.selectAll();
					    ImagenCroop.crooper.disable();

			  		},200);
				  
			  	};
			});

	},function(){
		//agregarElemento("#modeloCargaEspecie","datosEspecie","Nueva Especie");
		var $contenidoFormulario = clonar($("#modeloCargaEspecie"),"datosEspecie");
		lanzarModal("#modalCarga","Nueva Especie",$contenidoFormulario,function(){
			enviarElemento($("#datosEspecie"),COMPLEJO);
		});
ImagenCroop.inicializar("divDragNDrop","divContenedorImagen","imagen","botonCambiarImagen");
		activarSugerencias(camposAutocompletados,$("#datosEspecie"));

	});



	

	

	/*Fin Definicion de las tablas de datos*/

	$("#contenedorOpciones").css({"min-height":$("#secciones").height()+"px"});
	diferencia = $("#secciones").height()-$("#contenedorOpciones").height();
	var listaOpciones = $("#secciones").find(".list-group-item");
	for (var i = 0; i < listaOpciones.length; i++) {
		(function($elemento){
			$elemento.click(function(){
				cargarOpciones($elemento.attr("id"));
			});
		}($(listaOpciones[i])));

	};
//	ImagenCroop.inicializar(idHandler,idContenedorImagen,idImagen,idBotonCambiarImagen);
});

function cargarOpciones(opcion){
	anteriorSeleccionado = seleccionado;
	seleccionado = opcion;
	$("#"+anteriorSeleccionado).removeClass("active");
	$("#contenido"+(anteriorSeleccionado.charAt(0).toUpperCase() + anteriorSeleccionado.slice(1))).addClass("oculto");
	$("#"+seleccionado).addClass("active");
	$("#contenido"+(opcion.charAt(0).toUpperCase() + opcion.slice(1))).removeClass("oculto");
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

function clonar($elemento,idElemento,datos){
	var $formulario = $elemento.clone();
	$formulario.attr("id",idElemento);
	$formulario.removeClass("oculto");
	if (datos!=null) {
		var nombres = Object.keys(datos);
		nombres.map(function(elemento){
			$($formulario.find("[name|="+elemento+"]")[0]).val(datos[elemento]);
		});
	};
	return $formulario;
}

/*Operaciones de las tablas*/

/*
function agregarFormaBiologica(idModelo,idFormulario,titulo){
	var $contenidoFormulario = clonar($("#modeloCargaFormaBiologica"),"datosFormaBiologica");
	lanzarModal("#modalCarga","Nueva Forma Biológica",$contenidoFormulario,enviarFormaBiologica);
}

*/




function agregarElemento(idModelo,idFormulario,titulo){
	var $contenidoFormulario = clonar($(idModelo),idFormulario);
	lanzarModal("#modalCarga",titulo,$contenidoFormulario,function(){
		enviarElemento($("#"+idFormulario));
	});
}


function eliminarElemento($datos){
	$("#modalCarga").modal("hide");
	//var $datos = $("#datosFormaBiologica");
	var nombre = $datos.find("[name|=nombre]")[0].value;
	var tipoElemento = $datos.find("[name|=tipoElemento]")[0].value;
	var nombreTabla = $datos.find("[name|=nombreTabla]")[0].value;
	
	mostrarMensajeConfirmacion("Estas Seguro?","Esta seguro que desea eliminar '"+nombre+"' ?",function(){
		var identificador = $datos.find("[name|=id]")[0].value;
		$.post( "baseDeDatos/bajaElemento", { id: identificador, tipo: tipoElemento})
			.done(function( respuesta ){
				var rta = JSON.parse(respuesta);
				if (rta.codigo == CODIGO_EXITO) {
					mostrarMensajeExito(rta.mensaje);
					var rowSeleccionadas = ManejadorTablas.tablas[nombreTabla].data().filter(function(elemento){
						return parseInt(elemento[1])==rta.objeto.id;
					});
					if (rowSeleccionadas.length != 0 ) {
						var indice = ManejadorTablas.tablas[nombreTabla].data().indexOf(rowSeleccionadas[0]);
						ManejadorTablas.tablas[nombreTabla].row(indice).remove().draw();
					}
					$("#modalCarga").modal("hide");
				}else{
					mostrarMensajeError(rta.mensaje);
				}
			});			
	},function(){});

}

function enviarElemento($datos,complejo){
	//var $datos = $("#datosFormaBiologica");

	var complejo = complejo | SIMPLE;

	if(validarCampos($datos)){

		var nombre = $datos.find("[name|=nombre]")[0].value;
		var identificador = $datos.find("[name|=id]")[0].value;
		var tipoElemento = $datos.find("[name|=tipoElemento]")[0].value;
		var nombreTabla = $datos.find("[name|=nombreTabla]")[0].value;
		var objeto = {id: identificador, tipo: tipoElemento,nombre: nombre};
		if (complejo) {
			objeto.forma = $datos.find("[name|=forma]")[0].value;
			objeto.tipoBiologico = $datos.find("[name|=tipo]")[0].value;
			objeto.estado = $datos.find("[name|=estado]")[0].value;
			objeto.distribucion = $datos.find("[name|=distribucion]")[0].value;
			objeto.familia = $datos.find("[name|=familia]")[0].value;
			objeto.indice = $datos.find("[name|=indice]")[0].value;
			objeto.forrajera = ($datos.find("[name|=forrajera]")[0].checked)? 1 : 0;
			objeto.imagen = ImagenCroop.obtenerImagen();
			if (ImagenCroop.hayImagen) {
				objeto.coodenadasImagen = ImagenCroop.obtenerCoordenadas();
			};

		};
		$.ajax({
	        data: objeto,
	        type: "POST",
	        url: "baseDeDatos/altaElemento",
	        contentType: "application/x-www-form-urlencoded charset=utf-8",
	  		success: function(respuesta){
	  			var rta = JSON.parse(respuesta);
				if (rta.codigo == CODIGO_EXITO) {
					mostrarMensajeExito(rta.mensaje);
					var rowSeleccionadas= ManejadorTablas.tablas[nombreTabla].data().filter(function(elemento){
						return parseInt(elemento[1])==rta.objeto.id;
					});
					if (rowSeleccionadas.length != 0 ) {
						var indice = ManejadorTablas.tablas[nombreTabla].data().indexOf(rowSeleccionadas[0]);
						ManejadorTablas.tablas[nombreTabla].row(indice).remove().draw();
						if (complejo) {
							ManejadorTablas.tablas[nombreTabla].row.add( [
								rowSeleccionadas[0][0].toString(),
						        rta.objeto.id.toString(),
						        rta.objeto.nombre,
						        objeto.familia,
						        objeto.forma,
						        objeto.tipoBiologico,
						        objeto.distribucion,
						        objeto.indice,
						        objeto.forrajera,
						        objeto.estado
						    ] ).draw();

						}else{
							ManejadorTablas.tablas[nombreTabla].row.add( [
								rowSeleccionadas[0][0].toString(),
						        rta.objeto.id.toString(),
						        rta.objeto.nombre
						    ] ).draw();	
						}
						ManejadorTablas.tablas[nombreTabla].draw();
					}else{

						var contador = ManejadorTablas.tablas[nombreTabla].rows()[0].length;
						contador++;
						if (complejo) {
							ManejadorTablas.tablas[nombreTabla].row.add( [
								contador,
						        rta.objeto.id.toString(),
						        rta.objeto.nombre,
						        objeto.familia,
						        objeto.forma,
						        objeto.tipoBiologico,
						        objeto.distribucion,
						        objeto.indice,
						        objeto.forrajera,
						        objeto.estado
						    ] ).draw();

						}else{

						
					    ManejadorTablas.tablas[nombreTabla].row.add( [
					        contador,
					        rta.objeto.id,
					        nombre
					    ] ).draw();

						}
					    
					    ManejadorTablas.tablas[nombreTabla].page('last').draw( false );
						
					}
					$("#modalCarga").modal("hide");
				}else{
					mostrarMensajeError(rta.mensaje);
				}

	  		}
		});
		// $.post( "baseDeDatos/altaElemento", objeto)
		// 	.done(function( respuesta ){
		// 		var rta = JSON.parse(respuesta);
		// 		if (rta.codigo == CODIGO_EXITO) {
		// 			mostrarMensajeExito(rta.mensaje);
		// 			var rowSeleccionadas= ManejadorTablas.tablas[nombreTabla].data().filter(function(elemento){
		// 				return parseInt(elemento[1])==rta.objeto.id;
		// 			});
		// 			if (rowSeleccionadas.length != 0 ) {
		// 				var indice = ManejadorTablas.tablas[nombreTabla].data().indexOf(rowSeleccionadas[0]);
		// 				ManejadorTablas.tablas[nombreTabla].row(indice).remove().draw();
		// 				if (complejo) {
		// 					ManejadorTablas.tablas[nombreTabla].row.add( [
		// 						rowSeleccionadas[0][0].toString(),
		// 				        rta.objeto.id.toString(),
		// 				        rta.objeto.nombre,
		// 				        objeto.familia,
		// 				        objeto.forma,
		// 				        objeto.tipoBiologico,
		// 				        objeto.distribucion,
		// 				        objeto.indice,
		// 				        objeto.forrajera,
		// 				        objeto.estado
		// 				    ] ).draw();

		// 				}else{
		// 					ManejadorTablas.tablas[nombreTabla].row.add( [
		// 						rowSeleccionadas[0][0].toString(),
		// 				        rta.objeto.id.toString(),
		// 				        rta.objeto.nombre
		// 				    ] ).draw();	
		// 				}
		// 				ManejadorTablas.tablas[nombreTabla].draw();
		// 			}else{

		// 				var contador = ManejadorTablas.tablas[nombreTabla].rows()[0].length;
		// 				contador++;
		// 				if (complejo) {
		// 					ManejadorTablas.tablas[nombreTabla].row.add( [
		// 						contador,
		// 				        rta.objeto.id.toString(),
		// 				        rta.objeto.nombre,
		// 				        objeto.familia,
		// 				        objeto.forma,
		// 				        objeto.tipoBiologico,
		// 				        objeto.distribucion,
		// 				        objeto.indice,
		// 				        objeto.forrajera,
		// 				        objeto.estado
		// 				    ] ).draw();

		// 				}else{

						
		// 			    ManejadorTablas.tablas[nombreTabla].row.add( [
		// 			        contador,
		// 			        rta.objeto.id,
		// 			        nombre
		// 			    ] ).draw();

		// 				}
					    
		// 			    ManejadorTablas.tablas[nombreTabla].page('last').draw( false );
						
		// 			}
		// 			$("#modalCarga").modal("hide");
		// 		}else{
		// 			mostrarMensajeError(rta.mensaje);
		// 		}

		// });
	}
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


/*Fin Operaciones de las tablas*/


//  tablaFormaBiologicas = $("#tablaFormaBiologica").DataTable( {"lengthChange": false,"pageLength": 7,"language": {
//   "zeroRecords": "Busqueda sin resultados","emptyTable": "No hay Formas Biológicas que mostrar","search": "Buscar","info": "Mostrando Página _PAGE_ de _PAGES_","paginate": {
//     "previous": "Anterior","next":"Siguiente"}
//   }});

// $('#tablaFormaBiologica tbody').on( 'click', 'tr', function () {
// 		tablaFormaBiologicas.$('tr.selected').removeClass('selected');
//         $(this).addClass('selected');
//         var nombre = $($(this).find("td")[2]).text();
//         var id = $($(this).find("td")[1]).text();
//         var $contenidoFormulario = clonar($("#modeloCargaFormaBiologica"),"datosFormaBiologica",{"nombre":nombre,"id":id});
// 		lanzarModal("#modalCarga","Editar Forma Biológica",$contenidoFormulario,enviarFormaBiologica,eliminarFormaBiologica);
//     } );



// var agregarForma = $('<div class="divBoton botonAgregar"><a><i class="fa fa-plus"></i> Agregar</a></div>');
// agregarForma.click(function(){
// 		agregarFormaBiologica();
// });
// $("#tablaFormaBiologica_filter").before(agregarForma);

//function(nombreTabla,idTabla,callbackClicRow,callbackAgregar)