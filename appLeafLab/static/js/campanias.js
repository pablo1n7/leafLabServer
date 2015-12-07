var arregloCampanias = [];
var setEspecies = new Set();
var setCampania = new Set();
var campaniaActiva = null;
var especieActiva = null;
//var setEspecies = new Set(["Ada", "Java", "JavaScript", "Brainfuck", "LOLCODE", "Node.js", "Ruby on Rails"]);

$(document).ready(function() {

	verMapa();
	inicializarDatos();

	var input = document.getElementById("especieInput");
	new Awesomplete(input, {
		minChars: 1,
		maxItems: 5,
		list: Array.from(setEspecies)
	});

	var input = document.getElementById("campaniaInput");
	new Awesomplete(input, {
		minChars: 1,
		maxItems: 5,
		list: Array.from(setCampania)
	});


	window.addEventListener("awesomplete-selectcomplete", function(e){
		console.warn("Filtrando");
		if (e.target.name =="especie"){
			//alert($(e.target).val());
			especieActiva = $(e.target).val();
			$("#especieAplicadaNombre").empty();
			$("#especieAplicadaNombre").append(especieActiva);
			$("#especieAplicada").removeClass("oculto");
			$("#especieInput").val("");			
			
			if (campaniaActiva == null) {
				arregloCampanias.map(function(camp) {
					camp.filtrarEspecies(especieActiva);
				});	
			}else{

				campaniaActiva.filtrarEspecies(especieActiva);
			}
			

		}else{
			campaniaActiva = arregloCampanias.filter(function(c){
				return c.nombre == $(e.target).val();
			})[0];
			$("#campaniaAplicadaNombre").empty();
			$("#campaniaAplicadaNombre").append(campaniaActiva.nombre);
			$("#campaniaAplicada").removeClass("oculto");
			$("#campaniaInput").val("");
			arregloCampanias.map(function(camp){
				if (camp.nombre != campaniaActiva.nombre) {
					camp.transectas.map(function(tr){
						tr.marcadores.map(function(m){
							m.setVisible(false);
							m.setIcon("http://maps.google.com/mapfiles/ms/icons/green-dot.png");
						});
					});
				}else{
					if (especieActiva==null) {
					campaniaActiva.transectas.map(function(tr){
						tr.marcadores.map(function(m){
								m.setIcon("http://maps.google.com/mapfiles/ms/icons/blue-dot.png");
							});
						});
					};
				};
			});	

		}
	}, false);
});

function inicializarDatos(){
	if(map){
		arregloCampanias.map(function(camp){
			camp.transectas.map(function(tr){
				tr.marcadores = dibujarTransecta(tr.coordenadas);
				tr.especiesTransecta.map(function(esp){
					var nombreEspecies = Object.keys(esp.especies);
					nombreEspecies.map(function(nombre){
						setEspecies.add(nombre);
					});
				});
			});
		});
	}else{
		setTimeout(inicializarDatos,1000);
	}
}

/*
estructura de info:
			id: unEntero,
			nombre: unaCadena,
			transectas: unArregloTransectas
*/


var Campania = function(informacion){
	var _this = this;

	this.id = informacion.id;
	this.nombre = informacion.nombre;
	this.transectas = informacion.transectas;
	this.centro = null;

	this.obtenerCentro = function() {
		if (_this.centro == null) {
			var arregloCentrosCampanias = [];
			_this.transectas.map(function(tr){
				arregloCentrosCampanias.push(calcularCentroTransecta(tr.coordenadas));
			});
			_this.centro = centrarCampania(arregloCentrosCampanias);
		};	
		return _this.centro;
	};

	this.filtrarEspecies = function(especie){
		_this.transectas.map(function(tr){
			tr.marcadores.map(function(m){
				m.setVisible(false);
				m.setIcon("http://maps.google.com/mapfiles/ms/icons/green-dot.png");
			});
		});

		_this.transectas.map(function(tr){

			tr.especiesTransecta.map(function(et){
				if(et.especies.hasOwnProperty(especie)){
					et.especies[especie].map(function(i){
						tr.marcadores[i].setVisible(true);
						tr.marcadores[i].setIcon("http://maps.google.com/mapfiles/ms/icons/blue-dot.png");
					});
				}
			});
		});
	};

	// this.transectas.map(function(tr){
	// 	dibujarTransecta(tr.coordenadas);
	// });
};

var reconstruirCampania = function(infoCampania){
	setCampania.add(infoCampania.nombre);
	arregloCampanias.push(new Campania(infoCampania));
};

var eliminarFiltroEspecie = function(){
	especieActiva = null;
	$("#especieAplicada").addClass("oculto");
	if(campaniaActiva == null){
		marcadores.map(function(m) {
			if (!m.hasOwnProperty("strokeColor")) {
				m.setVisible(true);
				m.setIcon("http://maps.google.com/mapfiles/ms/icons/green-dot.png");
			};
		});
	}else{

		campaniaActiva.transectas.map(function(tr){
			tr.marcadores.map(function(m){
				m.setIcon("http://maps.google.com/mapfiles/ms/icons/blue-dot.png");
				m.setVisible(true);
			});
		});

	}
}

var eliminarFiltroCampania = function(){
	campaniaActiva = null;
	$("#campaniaAplicada").addClass("oculto");
	if(especieActiva == null){
		marcadores.map(function(m) {
			if (!m.hasOwnProperty("strokeColor")) {
				m.setVisible(true);
				m.setIcon("http://maps.google.com/mapfiles/ms/icons/green-dot.png");
			};
		});
	}else{
		arregloCampanias.map(function(c){
			c.filtrarEspecies(especieActiva);
		});
	}
}