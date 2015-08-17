const CODIGO_ERROR = 500;
const CODIGO_EXITO = 200;
const COMPLEJO = 1;
const SIMPLE = 0;
const CANTIDAD_PUNTOS = 11;

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