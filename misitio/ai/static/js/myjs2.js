/* Toda funcion que haga alusion a AJAX no hay que subirla a PythonAnywhere */
/* pues dará un error 404 */
/* ------------------ */
function llenacaja(){
	var fini = $('#datepicker').val();
	var fini = fini.slice(6,10)+"-"+fini.slice(0, 2)+"-"+fini.slice(3,5);
   	document.getElementById("datepicker").value=fini;
	}


function llenacaja2(){
	var fenac = $('#datepicker2').val();
	var fenac = fenac.slice(6,10)+"-"+fenac.slice(0, 2)+"-"+fenac.slice(3, 5);
   	document.getElementById("datepicker2").value=fenac;
	}


function prueba() {
	var x = document.getElementById("rut").value
    alert("!! Entró al MYJS.JS ¡¡"+x);
    document.getElementById("rut").focus();
    document.getElementById("rut").style.border = '2px solid red';
}

function validaemail(email) {
	/*alert("email llegó con :"+email);*/
	if(email=="correo"){ 
    	var x = document.getElementById("correo").value
	} else {
    	var x = document.getElementById("correo_apod").value
	}

    if(x!='') {
        var expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if ( !expr.test(x) ) {
            alert("Error: La dirección de correo " + x + " es incorrecta.");
            document.getElementById("correo").value = "";
        }
    }
}

function validarut_cui() {
	if(document.getElementById("extran").checked) { 	
		return true;
	} else {	
		validarut(); 
		/* siexiste() ---(AJAX) */
 	}
}


function separadordemiles(input) {
	var num = input.value.replace(/\./g,'');
	/* alert(num); */
}

/* valida rut del paciente desde FICHA_PACIENTES.HTML */
function validarut() {
	var rut = document.getElementById("rut").value 
	document.getElementById("rut").value=rut.toUpperCase()
	if (rut!='') {
		var rexp = new RegExp(/^([0-9])+\-([kK0-9])+$/);
		if(rut.match(rexp)){
			var RUT = rut.split("-");
			//var elRut = RUT[0].toArray();
			var elRut = RUT[0].split('');
			var factor = 2;
			var suma = 0;
			var dv;
			for(i=(elRut.length-1); i>=0; i--){
				factor = factor > 7 ? 2 : factor;
				suma += parseInt(elRut[i])*parseInt(factor++);
			}
			dv = 11 -(suma % 11);
			if(dv == 11){
				dv = 0;
			}else if (dv == 10){
				dv = "K";
			}
			if(dv==0-0) {
				alert("El rut es incorrecto por formato digitado.!!");
				return false;
			}
			if(dv == RUT[1].toUpperCase()){
         		document.getElementById("rut").style.border = '';
           		document.getElementById("nombre").focus();
        		return true; 
			}else{         
        		document.getElementById("rut").style.border = '2px solid red';
           		document.getElementById("rut").focus();		
           		document.getElementById("rut").value = '';			
				alert("El rut es incorrecto.!!!");
				return false;
			}
		}else{  
		    document.getElementById("rut").style.border = '2px solid red';
           	document.getElementById("rut").focus();	  
           	document.getElementById("rut").value = ''; 
			alert("RUT incorrecto por formato digitado.!!!");
			return false;
		}
	}	
}

function siexiste2(rut) {
    $("#rut").focusout(function () {
    	var username = $(this).val();
    	console.log( $(this).val() );
    	$.ajax({
    	    url: '/siexisterut/',
    	    data: {'rut':rut},
    	    dataType: 'json',
    	 	success: function (data) {
    	    	if (data.is_taken) {
    	        	alert("rut ya existe.");
    	    	}
    	    }
    	});
    });
}


function siexiste(rut) {
    $("#rut").change(function () {
      var rut = $(this).val();
      alert("Llega a la funcion SIEXISTE :"+rut);
      $.ajax({
        url: '/siexisterut/',
        data: {
          'rut': rut
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert("A user with this RUT already exists.");
          }
        }
      });
    });
}

/* valida rut del apoderado desde ficha PACIENTE */
function validarut2() {
	var rut = document.getElementById("rut_apod").value 
	document.getElementById("rut_apod").value=rut.toUpperCase()
	if (rut!='') {
		var rexp = new RegExp(/^([0-9])+\-([kK0-9])+$/);
		if(rut.match(rexp)){
			var RUT = rut.split("-");
			//var elRut = RUT[0].toArray();
			var elRut = RUT[0].split('');
			var factor = 2;
			var suma = 0;
			var dv;
			for(i=(elRut.length-1); i>=0; i--){
				factor = factor > 7 ? 2 : factor;
				suma += parseInt(elRut[i])*parseInt(factor++);
			}
			dv = 11 -(suma % 11);
			if(dv == 11){
				dv = 0;
			}else if (dv == 10){
				dv = "K";
			}
				if(dv == RUT[1].toUpperCase()){
         			document.getElementById("rut_apod").style.border = '';
           			document.getElementById("nombre").focus();
				return true;
			}else{         
        		document.getElementById("rut_apod").style.border = '2px solid red';
           		document.getElementById("rut_apod").focus();		
           		document.getElementById("rut_apod").value = '';			
				alert("Rut incorrecto por Digito Verificador!!");
				return false;
			}

		}else{

		    document.getElementById("rut_apod").style.border = '2px solid red';
           	document.getElementById("rut_apod").focus();	  
           	document.getElementById("rut_apod").value = ''; 
			alert("RUT incorrecto por formato digitado!!");
			return false;
		}
	}	
}

function habilitadeshabilita(campo) {
	var estadoActual = document.getElementById(campo);
	if(estadoActual.disabled)   {
		estadoActual.disabled= false;
	} else {
		estadoActual.disabled= true;
    }
}


// obtiene el focus
function txt_onfocus(txt) {
    txt.style.backgroundColor = " ";
}

// pierde el focus
function txt_onchange(txt)
{
    txt.style.backgroundColor = " ";   
}


function upperCase() {
	var x=document.getElementById("rut").value
	document.getElementById("rut").value=x.toUpperCase()
}

function valida_fono() {
	var fon = document.getElementById("fono_cuid").value;
    if(fon!='') {
		if( (!/^([0-9])*$/.test(fon)) ) {
			alert("El formato del numero telefonico introducido es incorrecto.");
			document.getElementById("fono_cuid").style.border = '2px solid red';
			document.getElementById("fono_cuid").focus();
		}else{
			document.getElementById("fono_cuid").style.border = '';	
		}
	}
}


function confirmar_borrado(nombre) {
	var nombre = $('#nombre').val();
	if(confirm('¿Estas seguro de efectuar el borrado de: '+nombre)) {

	}
}

function confirmar_borrado2(nombre,id) {
	var nombre = document.getElementById("nombre").value; 
   if(confirm('¿Estas seguro de borrar a :'+nombre+' ?')) {
     	var request = $.ajax({
    	    type: "GET",
    	    url: "{% url 'EliminaPac' id %}",
    	    data: {
    	        "csrfmiddlewaretoken": "{{ csrf_token }}",
    	        "id": id                    
    	    },
    		});
   			request.done(function(response) {
   		});
 	}
}

function mayuscula(e) {
	e.value = e.value.toUpperCase();
}


function limpia() {
	document.getElementById("busca").value = " ";
}


function Ocultar() {
	if(document.getElementById('div1_id').style.display == 'none') {
 		document.getElementById('div0_id').style.display = 'block'; 
 		document.getElementById('div1_id').style.display = 'block'; 
 		document.getElementById('div2_id').style.display = 'block';
 		document.getElementById('div3_id').style.display = 'block'; 
		document.getElementById('div7_id').style.display = 'block'; 
		document.getElementById('div8_id').style.display = 'block'; 
		document.getElementById('div9_id').style.display = 'block'; 
		document.getElementById('div10_id').style.display = 'block'; 
		document.getElementById('div11_id').style.display = 'block'; 
		document.getElementById('div12_id').style.display = 'block'; 

 	} else {
 		document.getElementById('div0_id').style.display = 'none';
 		document.getElementById('div1_id').style.display = 'none';
 		document.getElementById('div2_id').style.display = 'none';
 		document.getElementById('div3_id').style.display = 'none';
 		document.getElementById('div7_id').style.display = 'none';
 		document.getElementById('div8_id').style.display = 'none';
 		document.getElementById('div9_id').style.display = 'none';
 		document.getElementById('div10_id').style.display = 'none';
 		document.getElementById('div11_id').style.display = 'none';
 		document.getElementById('div12_id').style.display = 'none'; 		
 	}
}

/* Valida FICHA de PAUTA*/ 
function ValidarForm() {
	var yace = document.getElementById("yace").value 
	var rut_t1 = document.getElementById("rut_t1").value 
	var rut_t2 = document.getElementById("rut_t2").value 
	var rut_t3 = document.getElementById("rut_t3").value 
	var tipo_turno1 = document.getElementById("tipo_turno1").value 
	var tipo_turno2 = document.getElementById("tipo_turno2").value 
	var tipo_turno3 = document.getElementById("tipo_turno3").value
	var reca_cui = document.getElementById("reca_cui").value


	if (yace == '6'){
		alert("No ha especificado la ESTADIA !!")
		document.getElementById('yace').focus()
		document.getElementById('yace').style.border = '2px solid red';		
		return false;	
	}

	if(rut_t1 == '0-0' && rut_t2 == '0-0' && rut_t3 == '0-0' ){
		alert("Error!!..no ha asignado CUIDADOR");
		return false;
	}

	if(rut_t1 != '0-0' && tipo_turno1 == '0'){
		alert("Error!!..todo cuidador debe tener su respectivo TIPO DE TURNO");
		document.getElementById('tipo_turno1').focus()
		document.getElementById('tipo_turno1').style.border = '2px solid red';		
		return false;
	}

	if(rut_t2 != '0-0' && tipo_turno2 == '0'){
		alert("Error!!..todo cuidador debe tener su respectivo TIPO DE TURNO");
		document.getElementById('tipo_turno2').focus()
		document.getElementById('tipo_turno2').style.border = '2px solid red';		
		return false;
	}

	if(rut_t3 != '0-0' && tipo_turno3 == '0'){
		alert("Error!!..todo cuidador debe tener su respectivo TIPO DE TURNO");
		document.getElementById('tipo_turno3').focus()
		document.getElementById('tipo_turno3').style.border = '2px solid red';		
		return false;
	}


	/* recargo x dia FIN DE SEMANA - DIA FESTIVO - NORMAL */
	if(reca_cui === "0"){
		alert("Defina si esta fecha es: NORMAL - DOMINGO - FESTIVO ");
		document.getElementById('reca_cui').focus()
		document.getElementById('reca_cui').style.border = '2px solid red';
		return false;
	}

}


function ValidaFichapac() {
	var medico = document.getElementById("medico").value 
	var fe_ini = document.getElementById("fe_ini").value 
	var fono_pcte = document.getElementById("fono_pcte").value 
	var valor_t1 = document.getElementById("valor_t1").value 
	var valor_t2 = document.getElementById("valor_t2").value 
	var valor_t3 = document.getElementById("valor_t3").value 
	var f_apod = document.getElementById("f_apod").value 
	var parentes = document.getElementById("parentes").value 
    var rut  = document.getElementById("rut").value
    var clasi = document.getElementById("clasi").value 
	var yace = document.getElementById("yace").value 
	var correo_apod = document.getElementById("correo_apod").value 
	var abono_ini = document.getElementById("valor_abono").value


	if(rut === "0" || rut === "" || rut === 0-0){
		alert("El RUT no debe estar en blanco o ser cero");
		document.getElementById('rut').focus()
		document.getElementById('rut').style.border = '2px solid red';
		return false;
	}

	if(medico === ""){
		alert("El nombre del MEDICO es obligatorio");
		document.getElementById('medico').focus()
		document.getElementById('medico').style.border = '2px solid red';
		return false;
	}
	if(fe_ini === ""){
		alert("La FECHA DE INICIO del paciente es obligatoria");
		document.getElementById('fe_ini').focus()
		document.getElementById('fe_ini').style.border = '2px solid red';
		return false;
	}
	if(fono_pcte === ""){
		alert("El FONO DEL PACIENTE es obligatorio");
		document.getElementById('fono_pcte').focus()
		document.getElementById('fono_pcte').style.border = '2px solid red';
		return false;
	}

	if(clasi === "0"){
		alert("LA CLASIFICACION es obligatoria");
		document.getElementById('clasi').focus()
		document.getElementById('clasi').style.border = '2px solid red';
		return false;
	}

	if(yace === "6"){
		alert("LUGAR DONDE SE OTORGA LA PRESTACION es obligatorio"); 
		document.getElementById('yace').focus()
		document.getElementById('yace').style.border = '2px solid red';
		return false;
	}


	if(valor_t1 === ""){
		alert("TARIFA DE MAÑANA es obligatoria");
		document.getElementById('valor_t1').focus()
		document.getElementById('valor_t1').style.border = '2px solid red';
		return false;
	}
	if(valor_t2 === ""){
		alert("TARIFA DE TARDE es obligatoria");
		document.getElementById('valor_t2').focus()
		document.getElementById('valor_t2').style.border = '2px solid red';
		return false;
	}
	if(valor_t3 === ""){
		alert("TARIFA DE NOCHE es obligatoria");
		document.getElementById('valor_t3').focus()
		document.getElementById('valor_t3').style.border = '2px solid red';
		return false;
	}

	if(f_apod === ""){
		alert("FONO APODERADO es obligatorio");
		document.getElementById('f_apod').focus()
		document.getElementById('f_apod').style.border = '2px solid red';
		return false;
	}


	if(parentes === ""){
		alert("El PARENTEZCO es obligatorio");
		document.getElementById('parentes').focus()
		document.getElementById('parentes').style.border = '2px solid red';
		return false;
	}

	if(correo_apod === ""){
		alert("El CORREO DEL APODERADO es obligatorio");
		document.getElementById('correo_apod').focus()
		document.getElementById('correo_apod').style.border = '2px solid red';
		return false;
	}

	if(abono_ini === "" || abono_ini  === "0" || abono_ini=== 'none') {
		document.getElementById('abono_inicial').style.border = '2px solid red'; 
		alert("Una vez grabada esta ficha, deberá volver a la misma e ingresar el monto ABONO INICIAL");
	} 

}

function ValidaFichacui() {
	var tipo = document.getElementById("tipo").value 
	var fe_ini = document.getElementById("fe_ini").value  
	var direccion = document.getElementById("direccion").value
	var fono_cuid = document.getElementById("fono_cuid").value 
	var apago1 = document.getElementById("apago1").value 
	var apago2 = document.getElementById("apago2").value 
	var apago3 = document.getElementById("apago3").value 
    var rut    = document.getElementById("rut").value
    var nombre = document.getElementById("nombre").value
    var fono_cuid = document.getElementById("fono_cuid").value

	if(nombre === ""){
		alert("El NOMBRE es obligatorio");
		document.getElementById('nombre').focus()
		document.getElementById('nombre').style.border = '2px solid red';
		return false;
	}

	if(tipo === '0'){
		alert("El TIPO DE CONTRATO es obligatorio");
		document.getElementById('tipo').focus()
		document.getElementById('tipo').style.border = '2px solid red';
		return false;
	}

	if(direccion === ''){
		alert("La DIRECCION es obligatoria");
		document.getElementById('direccion').focus()
		document.getElementById('direccion').style.border = '2px solid red';
		return false;
	}


	if(fe_ini === ''){
		alert("La FECHA DE INICIO es obligatoria");
		document.getElementById('fe_ini').focus()
		document.getElementById('fe_ini').style.border = '2px solid red';
		return false;
	}

	if(fono_cuid === ''){
		alert("El FONO es obligatorio");
		document.getElementById('fono_cuid').focus()
		document.getElementById('fono_cuid').style.border = '2px solid red';
		return false;
	}

	if(apago1 === "0" || apago1 === ""){
		alert("TARIFA DE MAÑANA es obligatoria");
		document.getElementById('apago1').focus()
		document.getElementById('apago1').style.border = '2px solid red';
		return false;
	}
	if(apago2 === "0" || apago2 === ""){
		alert("TARIFA DE TARDE es obligatoria");
		document.getElementById('apago2').focus()
		document.getElementById('apago2').style.border = '2px solid red';
		return false;
	}
	if(apago3 === "0" || apago3 === ""){
		alert("TARIFA DE NOCHE es obligatoria");
		document.getElementById('apago3').focus()
		document.getElementById('apago3').style.border = '2px solid red';
		return false;
	}
}

function ValidaFicha_anti() {
	var tipabon = document.getElementById("abon").value
	var banco =   document.getElementById("banco").value
	var fe_che =  document.getElementById("fecha_cheque").value

	if(tipabon === "0"){
		alert("TIPO DE ABONO es obligatorio");
		document.getElementById('abon').focus()
		document.getElementById('abon').style.border = '2px solid red';
		return false;
	}

	if(tipabon == "2" && banco == "9"){
		alert("Si el abono es CHEQUE, entonces complete los datos de este");
		document.getElementById('abon').focus()
		document.getElementById('cheque').style.border = '2px solid red';
		document.getElementById('banco').style.border = '2px solid red';
		document.getElementById('fecha_cheque').style.border = '2px solid red';
		return false;
	} 
}


function confirmaelimpac(nombre,id){
	var opcion=confirm('¿Seguro de borrar a paciente: '+nombre+' ?');
	if (opcion == true) {
      	var request = $.ajax({
            type: 'GET',
            url: "{% url 'Eliminapac_nuevo' %}",
	 	    data: {"id": id },
    	    /*    	
	 	    data: {
    	        "csrfmiddlewaretoken": "{{ csrf_token }}",
    	        "id": id },
			*/
        });
        alert("No funcó!! :"+request);
        request.done(function(response) {
            alert("Registro eliminado");
        });	

 	}else{
		return false;
	}
}

/* para mostrar contraseña durante la digitacion */
function mostrarPassword(){
		var cambio = document.getElementById("txtPassword");
		if(cambio.type == "password"){
			cambio.type = "text";
			$('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
		}else{
			cambio.type = "password";
			$('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
		}
	} 
	
	$(document).ready(function () {
	//CheckBox mostrar contraseña
	$('#ShowPassword').click(function () {
		$('#Password').attr('type', $(this).is(':checked') ? 'text' : 'password');
	});
});


function validarFormatoFecha() {
	var fe_ini = document.getElementById("fe_ini").value
    var RegExPattern = /^\d{1,4}\-\d{1,2}\-\d{1,2}$/;
    if (fe_ini.match(RegExPattern)) {
    	document.getElementById("fe_ini").style.border = '';
        return true;
    } else {
		document.getElementById('fe_ini').style.border = '2px solid red';
      	alert("Error!! formato de FECHA INICIO debe ser aaaa-mm-dd, los separadores son signos menos");
      	return false;
    }
}

function validarFormatoFecha2() {
	var fe_nac = document.getElementById("fe_nac").value
    var RegExPattern = /^\d{1,4}\-\d{1,2}\-\d{1,2}$/;
    if (fe_nac.match(RegExPattern)) {
    	document.getElementById("fe_nac").style.border = '';
        return true;
    } else {
		document.getElementById('fe_nac').style.border = '2px solid red';
      	alert("Error!! formato de FECHA NACIMIENTO debe ser aaaa-mm-dd, los separadores son signos menos");
  		return false;    	
    }
}

/* valida fecha cheque - ficha paciente */
function validarFormatoFecha3() {
	var fe_nac = document.getElementById("fecha_cheque").value
    var RegExPattern = /^\d{1,4}\-\d{1,2}\-\d{1,2}$/;
    if (fe_nac.match(RegExPattern)) {
    	document.getElementById("fecha_cheque").style.border = '';
        return true;
    } else {
		document.getElementById('fecha_cheque').style.border = '2px solid red';
      	alert("Error!! formato de FECHA CHEQUE debe ser aaaa-mm-dd, los separadores son signos menos (solo en caso de cheques)");
  		return false;    	
    }
}


function validarchivo() {
	/* var archivo = $('input[name="foto"]').val();  */
	var archivo = document.getElementById("fotito").value
	if(archivo == ""){
		alert("!! No ha seleccionado archivo para subir.. !! ");
		return false;
	}else{
		alert("El archivo próximo a subir es: "+archivo)
		return true;
	}
}	

/* forma de pago */
function validabono() {
	var pagacon = document.getElementById("abon").value
	if(pagacon != "2") {
		document.getElementById("cheque").value = ""
		document.getElementById("bco").value = "9"
		document.getElementById("fecha_cheque").value = ""

		document.getElementById("cheque").readOnly = true;
		document.getElementById("bco").readOnly = true;
		document.getElementById("fecha_cheque").readOnly = true;

	}else{
		document.getElementById("cheque").readOnly = false;
		document.getElementById("bco").readOnly = false;
		document.getElementById("fecha_cheque").readOnly = false;
	}
}	

