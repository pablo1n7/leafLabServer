const CODIGO_ERROR = 500;
const CODIGO_EXITO = 200;
const COMPLEJO = 1;
const SIMPLE = 0;
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

	
	// $(id).unbind('keyup');
 // 	$(id).bind('keyup', function (e) {
	//   var key = e.keyCode || e.which;
	//   if (key === 13) {
	//     $($(id+" .btn-primary")[0]).click();	   
	//   };
	// });

 	$(id).modal("show");
	$($modalBody.find("input")[1]).focus();
}


function actualizarValor(rango){
	$(rango.nextElementSibling).text(rango.value);
}