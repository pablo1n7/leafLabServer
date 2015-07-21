// Requiere:
//			Jquery
//			JCroop

var ImagenCroop = (function(){
	var hayImagen = false;
	var crooper = null;
	var idDroper = "";
	var idContenedorImagen = "";
	var idImagen = "";
	var idBotonCambiarImagen = "";

	var inicializar = function(idHandler,idContenedorImagen,idImagen,idBotonCambiarImagen){
			ImagenCroop.idDroper = idHandler;
			ImagenCroop.idContenedorImagen = idContenedorImagen;
			ImagenCroop.idImagen = idImagen;
			ImagenCroop.idBotonCambiarImagen = idBotonCambiarImagen;
			$("#"+ImagenCroop.idBotonCambiarImagen).click(function(){
				ImagenCroop.activarCargaImagen();
			});
			ImagenCroop.activarDropImagen();
		};

	var activarDropImagen = function(){
			var divContenedor = document.getElementById(ImagenCroop.idDroper);
			divContenedor.addEventListener("dragover", function(e){e.preventDefault();}, true);
			divContenedor.addEventListener("drop", function(e){
				e.preventDefault(); 
				cargarImagen(e.dataTransfer.files[0]);
			}, true);
		};

	var instanciarImagen = function(src){
		ImagenCroop.hayImagen = true;
		$("#"+ImagenCroop.idImagen).attr("src",src);
		$("#"+ImagenCroop.idContenedorImagen).removeClass("oculto");
		$("#"+ImagenCroop.idDroper).addClass("oculto");
        ImagenCroop.crooper = jQuery.Jcrop($("#"+ImagenCroop.idImagen)[0],{
            bgColor:     "black",
            bgOpacity:   .4,
            setSelect:   [ 200, 200, 300, 300 ],
            aspectRatio: 1
        });
	};

	var cargarImagen = function(imagen){
			if(!imagen.type.match(/image.*/)){
				mostrarMensajeError("El Elemento seleccionado no es una imagen!: "+ imagen.type);
				return;
			}
			var reader = new FileReader();
			reader.onload = function(e){
				ImagenCroop.instanciarImagen(e.target.result)
			};
			reader.readAsDataURL(imagen);
		};

	var activarCargaImagen =function(){
			ImagenCroop.crooper.destroy();
			ImagenCroop.hayImagen = false;
			$("#"+ImagenCroop.idContenedorImagen).addClass("oculto");
			$("#"+ImagenCroop.idImagen).attr("src","");
			$("#"+ImagenCroop.idDroper).removeClass("oculto");
		};

	var selectAll = function(){
		var alto = $("#"+ImagenCroop.idImagen).height();
		var ancho = $("#"+ImagenCroop.idImagen).width();
		ImagenCroop.crooper.setSelect([0,0,ancho,alto]);

	};

	var obtenerImagen = function(){
		if(ImagenCroop.hayImagen)
			return $("#"+ImagenCroop.idImagen).attr("src");
		return null;
	};

	var obtenerCoordenadas = function(){
			var coord = ImagenCroop.crooper.tellSelect();
			var altoImg = $("#"+ImagenCroop.idImagen).height();
			var anchoImg = $("#"+ImagenCroop.idImagen).width();

			if((isNaN(coord.x2) && isNaN(coord.y2)) || (coord.y2 == coord.y) && (coord.x2 == coord.x) ){
				var x = 0;
				var y = 0;
				var ancho = 1;
				var alto = 1;
			}else{
				var x = (coord.x / anchoImg);
				var y = (coord.y / altoImg);
				var ancho = (coord.w / anchoImg);
				var alto = (coord.h / altoImg);
			}
			return{
				x:x,
				y:y,
				ancho:ancho,
				alto:alto
			}
		};

	return{
		inicializar:inicializar,
		activarCargaImagen:activarCargaImagen,
		activarDropImagen:activarDropImagen,
		cargarImagen:cargarImagen,
		selectAll:selectAll,
		instanciarImagen:instanciarImagen,
		obtenerCoordenadas:obtenerCoordenadas,
		obtenerImagen:obtenerImagen,
		hayImagen:hayImagen,
	}
}());