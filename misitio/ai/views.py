# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from misitio.ai.forms import CuidadoresForm
from misitio.ai.forms import PacientesForm
from misitio.ai.forms import ApoderadosForm
from misitio.ai.forms import ParamForm
from misitio.ai.forms import PautaForm
from misitio.ai.models import Cuidadores,Pacientes,Apoderados
from misitio.ai.models import Param,Pauta
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from os import remove
#
from datetime import datetime,timedelta
from django.db import DatabaseError, transaction
from django.db import connection
import calendar

def principal(request):
    variable1 = 'PAGINA PRINCIPAL'
    logo = "/static/img/Logo_AsistenciaIntegral.jpeg"
    context ={"variable1":variable1,"logo_corp":logo,}
    return render(request,'principal.html',context)

def login_ini2(request):
    return HttpResponse("!! Sistema momentaneamente en etapa de pruebas y avance de desarrollo!!")

def login_ini(request):
    variable1 = 'Pantalla de Acceso al Sistema'
    error_log = 'ok'
    username = request.POST.get('username')
    password = request.POST.get('password') # valor del template
    user = auth.authenticate(username=username, password=password)
    if request.method == "POST":
        if user is not None and user.is_active:
    		# Correct password, and the user is marked "active"
            auth.login(request, user)

            return HttpResponseRedirect("principal")
        error_log = "error"
        context ={"variable1":variable1,"error_log":error_log,}
        return render(request,"login_ini.html",context)
    context ={
			'user':user,
			"variable1":variable1,
			"error_log":error_log,
	}
    #return HttpResponse("penultima linea"+str(STATIC_FILES))
    return render(request,'login_ini.html',context)


def log_out(request):
	logout(request)
	return redirect('login_ini')


def grid_cuidadores(request):
	variable1 = 'Despliegue de Cuidadores'
	cuidador = Cuidadores.objects.all().order_by('nombre')
	context = {
		"cuidadores":cuidador,
		"variable1":variable1,
	}
	return render(request,'grid_cuidadores.html',context)

def grid_apoderados(request):
	variable1 = 'Despliegue de Apoderados'
	apoderado = Apoderados.objects.all().order_by('nombre')
	context = {
		"apoderados":apoderado,
		"variable1":variable1,
	}
	return render(request,'grid_apoderados.html',context)

def grid_pacientes(request):
	variable1 = 'Despliegue de Pacientes'
	paciente = Pacientes.objects.all().order_by('nombre')
	context = {
		"pacientes":paciente,
		"variable1":variable1,
	}
	return render(request,'grid_pacientes.html',context)


def grid_param(request):
	variable1 = 'Despliegue de Parametros del Sistema'
	param =  Param.objects.all().order_by('tipo','descrip')

	context = {
		"param":param,
		"variable1":variable1,
	}
	return render(request,'grid_param.html',context)

#busca cuidador
def grid_cuidadorBusca(request):
	variable1 = 'Buscando Cuidadores'
	queryset = request.GET.get('buscar').strip()
	cuidador = Cuidadores.objects.all().order_by('nombre')
	cuidador = Cuidadores.objects.filter(Q(nombre__icontains=queryset))
	context = {
		"cuidadores":cuidador,
		"variable1":variable1,
	}
	return render(request,'grid_cuidadores.html',context)

def grid_pacienteBusca(request):
	variable1 = 'Buscando Paciente'
	queryset = request.GET.get('buscar').strip()
	paciente = Pacientes.objects.all().order_by('nombre')
	paciente =  Pacientes.objects.filter(Q(nombre__icontains=queryset))
	context = {
		"pacientes":paciente,
		"variable1":variable1,
	}
	return render(request,'grid_pacientes.html',context)


def grid_paramBusca(request):
	variable1 = 'Buscando Parametro'
	buscar = request.GET.get('buscar').strip()
	check1 = request.GET.get('check1')
	#return HttpResponse("Viene con: "+str(queryset))
	param = Param.objects.all().order_by('tipo','descrip')
	if buscar != "":
		if check1 == None:
			param = Param.objects.filter(Q(tipo__icontains=buscar))
		else:
			param = Param.objects.filter(Q(descrip__icontains=buscar))
	context = {
		"param":param,
		"variable1":variable1,
		"buscar":buscar,
	}
	return render(request,'grid_param.html',context)


def ficha_cuidadores(request,id):
	variable1 = 'Ficha del Cuidador'
	variable2 = 'modifica_rut'
	obj = Cuidadores.objects.get(id=id)
	context = {
	   	"rut":obj.rut,
	   	"nombre":obj.nombre,
		"direccion":obj.direccion,
		"fe_ini":obj.fe_ini,
		"fono_cuid":obj.fono_cuid,
	   	"fono2_cuid":obj.fono2_cuid,
	   	"fe_nac":obj.fe_nac,
	   	"variable1":variable1,
	   	"variable2":variable2,
	}
	return render(request,'ficha_cuidadores.html',context)


def ficha_apoderados(request,id):
	variable1 = 'Ficha de Apoderado'
	variable2 = 'modifica_rut'
	obj = Apoderados.objects.get(id=id)
	context = {
	   	"rut":obj.rut,
	   	"nombre":obj.nombre,
		"direccion":obj.direccion,
		"fe_ini":obj.fe_ini,
		"fono_apod":obj.fono_apod,
	   	"fono2_apod":obj.fono2_apod,
	   	"variable1":variable1,
	   	"variable2":variable2,
	}
	return render(request,'ficha_apoderados.html',context)


#def ficha_pauta(request,id):
#	variable1 = 'Ficha de Pauta diaria'
#	variable2 = 'nomodifica_rut'
#	obj = Pauta.objects.get(id=id)
#	context = {
#	   	"rut":obj.rut,
#	   	"nombre":obj.paciente,
#		"fe_ini":obj.fe_ini,
#	   	"variable1":variable1,
#	   	"variable2":variable2,
#	}
#	return render(request,'ficha_pauta.html',context)


def EliminaCui(request,id):
	#return HttpResponse("Entró a EliminaCui")
	variable1 = 'Despliegue de Cuidadores'
	form = Cuidadores.objects.get(id=id)
	form.delete()
	return redirect('grid_cuidadores')	#redirige a la URL


def EliminaPac(request,id):
	#return HttpResponse("Entró a EliminaCui")
	variable1 = 'Eliminacion de Paciente desde la base de datos'
	form = Pacientes.objects.get(id=id)
	context = {
		'form':form,
		'variable1':variable1,
	}
	if request.method == "POST":
		form.delete()
		return redirect('grid_pacientes')	#redirige a la URL
	return render(request,'confirma_elimina.html',context)

def EliminaApod(request,id):
	variable1 = 'Despliegue de Pacientes'
	form = Apoderados.objects.get(id=id)
	form.delete()
	return redirect('grid_apoderados')	#redirige a la URL


def EliminaParam(request,id):
	form = Param.objects.get(id=id)
	if method == 'POST':
		form.delete()
		return redirect('grid_param')	#redirige a la URL
	return render(request,eliminar_registro.html,{'nombre':form.nombre})


def NuevoCui(request):
	variable1 = 'Agregando nueva Ficha de Cuidador'
	variable2 = "modifica_rut"
	error_new = "ok"
	form = CuidadoresForm(request.POST or None)
	region  =  Param.objects.filter(tipo='REGI').order_by('descrip')
	comuna  =  Param.objects.filter(tipo='COMU').order_by('descrip')
	sexo    =  Param.objects.filter(tipo='SEXO').order_by('codigo')
	tipo    =  Param.objects.filter(tipo='CONTR').order_by('codigo') # Contratado - honorarios
	clasi   =  Param.objects.filter(tipo='CLASI').order_by('codigo') #
	instr	=  Param.objects.filter(tipo='INSTR').order_by('codigo')
	context = {
		'form':form,
		'variable1':variable1,
		'variable2':variable2,
		'region':region,
		'comuna':comuna,
		'sexo':sexo,
		'tipo':tipo,
		'clasi':clasi,
		'instr':instr,
		'error_new':error_new,
		}
	if request.method == "POST":
		cuidador = Cuidadores
		rut_x = request.POST.get('rut') # valor del template
		existe = cuidador.objects.filter(rut=rut_x).exists()
		#return HttpResponse("existe: "+str(existe))
		direcc_x = request.POST.get('direccion') # valor del template
		if existe == True:
			error_new = 'error1'
			context = {
				'form':form,
				'variable1':variable1,
				'variable2':variable2,
				'region':region,
				'comuna':comuna,
				'sexo':sexo,
				'tipo':tipo,
				'clasi':clasi,
				'instr':instr,
				'error_new':error_new,
			}
		else:
			if form.is_valid():
				cuidador = Cuidadores
				form.save()
				return redirect('grid_cuidadores')
	return render(request, 'ficha_cuidadores.html',context)


def NuevoApod(request):
	variable1 = 'Agregando nueva Ficha de Apoderado'
	variable2 = "modifica_rut"
	error_new = "ok"
	form = ApoderadosForm(request.POST or None)
	region    =  Param.objects.filter(tipo='REGI').order_by('descrip')
	comuna    =  Param.objects.filter(tipo='COMU').order_by('descrip')
	context = {
		'form':form,
		'variable1':variable1,
		'variable2':variable2,
		'region':region,
		'comuna':comuna,
		'error_new':error_new,
		}
	if request.method == "POST":
		apoderado = Apoderados
		rut_x = request.POST.get('rut') # valor del template
		existe = apoderado.objects.filter(rut=rut_x).exists()
		if existe == True:
			error_new = 'error1'
			context = {
				'form':form,
				'variable1':variable1,
				'variable2':variable2,
				'region':region,
				'comuna':comuna,
				'error_new':error_new,
			}
		else:
			if form.is_valid():
				apoderado = Apoderados
				form.save()
				return redirect('grid_apoderados')
	return render(request,'ficha_apoderados.html',context)


def siexisterut(request):
	paciente = Pacientes
	if request.method == 'GET':
		rut_x = request.GET.get('rut',None) # valor del template
		data = {
			'is_taken':paciente.objects.filter(rut=rut_x).exists()
		}
		return JsonResponse(data)


def NuevoPac(request):
	# Manda al formulario todos los campos vacios
	variable1 = 'Agregando nueva Ficha de Paciente'
	variable2 = "modifica_rut"
	error_new = "ok"
	form 	  =  PacientesForm(request.POST or None)
	region    =  Param.objects.filter(tipo='REGI').order_by('descrip')
	comuna    =  Param.objects.filter(tipo='COMU').order_by('descrip')
	sexo      =  Param.objects.filter(tipo='SEXO').order_by('codigo')
	cob       =  Param.objects.filter(tipo='COBR').order_by('codigo') # tipo de cobranza
	clasi     =  Param.objects.filter(tipo='PROC').order_by('codigo') # particular - instit.
	abon      =  Param.objects.filter(tipo='ABON').order_by('codigo') # Efec,Cheq,Tarj
	yace      = Param.objects.filter(tipo='YACE').order_by('-codigo') #Hosp.Domici.Cli

	context = {
		'form':form,
		'variable1':variable1,
		'variable2':variable2,
		'region':region,
		'comuna':comuna,
		'sexo':sexo,
		'cob':cob,
		'clasi':clasi,
		'abon':abon,
		'error_new':error_new,
		'yace':yace,
		'car_doc_cobro':"3",}
	if request.method == "POST":
		paciente = Pacientes    # modelo
		rut_x = request.POST.get('rut') # valor del template
		existe = paciente.objects.filter(rut=rut_x).exists()
		if existe == True:
			error_new = 'error1'
			context = {
				'form':form,
				'variable1':variable1,
				'variable2':variable2,
				'region':region,
				'comuna':comuna,
				'sexo':sexo,
				'cob':cob,
				'clasi':clasi,
				'abon':abon,
				'error_new':error_new,
				'yace':yace,
				'var_doc_cobro':var_doc_cobro,
			}
		else:
			if form.is_valid():
				paciente = Pacientes    # modelo
				form.save()
				return redirect('grid_pacientes')
	return render(request, 'ficha_pacientes.html',context)


def ActualizaCui(request,id):
	variable1 = 'Modifica Cuidador existente'
	variable2 = 'nomodifica_rut'
	cuidador  =  Cuidadores.objects.get(id=id)
	form = CuidadoresForm(request.POST,instance=cuidador)
	region    =  Param.objects.filter(tipo='REGI').order_by('descrip')
	comuna    =  Param.objects.filter(tipo='COMU').order_by('descrip')
	sexo      =  Param.objects.filter(tipo='SEXO').order_by('codigo')
	tipo      =  Param.objects.filter(tipo='CONTR').order_by('codigo') #tipo contrato
	clasi     =	 Param.objects.filter(tipo='CLASI').order_by('codigo') #Superior-interm.-stand
	instr	  =  Param.objects.filter(tipo='INSTR').order_by('codigo') # nivel educ.
	var_region = cuidador.region # entrega valor del registro Cuidadores
	var_comuna = cuidador.comuna # entrega valor del registro Cuidadores
	var_sex    = cuidador.sexo   # entrega valor del registro Cuidadores
	var_tip    = cuidador.tipo   # entrega valor del registro Cuidadores
	var_clasi  = cuidador.clasi  # entrega valor del registro Cuidadores
	var_instr  = cuidador.instr  # nivel educacional

	if  request.method == "POST":
		elim_foto_x = request.POST.get('elim_foto')
		if elim_foto_x == '0':  # elimina
			remove("misitio/ai/static/img/fotos/"+cuidador.rut+".jpg")

		if form.is_valid():
			form.save()
			return redirect('grid_cuidadores')

	form = CuidadoresForm(instance=cuidador)
	var_sex = cuidador.sexo # entrega valor del campo
	var_region = cuidador.region # entrega valor del campo
	var_comuna = cuidador.comuna # entrega valor del campo
	fotito = "/static/img/fotos/"+cuidador.rut+".jpg"
	context = {
		"variable1":variable1,
		"variable2":variable2,
		"form":form,
		"sexo":sexo,
		"region":region,
		"comuna":comuna,
		"clasi":clasi,
		"tipo":tipo,
		"instr":instr,
		"fotito":fotito,
		"id_x":id,
		"var_sex":var_sex,
		"var_region":var_region,
		"var_comuna":var_comuna,
		"var_tip":var_tip,
		"var_clasi":var_clasi,
		"var_instr":var_instr,
		}
	return render(request,'ficha_cuidadores.html',context)


def ActualizaApod(request,id):
	variable1 = 'Modifica Apoderado existente'
	variable2 = 'nomodifica_rut'
	apoderado =  Apoderados.objects.get(id=id)
	region    =  Param.objects.filter(tipo='REGI').order_by('descrip')
	comuna    =  Param.objects.filter(tipo='COMU').order_by('descrip')
	if request.method == "POST":
		form = ApoderadosForm(request.POST,instance=apoderado)

		region = Param()
		region.codigo = request.POST.get('regi')

		comuna = Param()
		comuna.codigo = request.POST.get('comu')

		if form.is_valid():
			form.save()
			return redirect('grid_apoderados')
		else:
			form = ApoderadosForm(instance = apoderado)
			var_region = apoderado.region # entrega valor del campo
			var_comuna = apoderado.comuna # entrega valor del campo
			context = {
				"variable1":variable1,
				"variable2":variable2,
				"form":form,
				"region":region,
				"comuna":comuna,
				"id_x":id,
				"var_region":var_region,
				"var_comuna":var_comuna,
			}
			render(request,'ficha_apoderados.html',context)
	else:
		form = ApoderadosForm(instance=apoderado) # trae el registro completo
		var_region = apoderado.region # entrega valor del campo
		var_comuna = apoderado.comuna # entrega valor del campo
		context = {
			"variable1":variable1,
			"variable2":variable2,
			"form":form,
			"region":region,
			"comuna":comuna,
			"id_x":id,
			"var_region":var_region,
			"var_comuna":var_comuna,
			}
	return render(request,'ficha_apoderados.html',context)


def ActualizaPac(request,id):
	error1= "ok"
	variable1 = 'Modifica Paciente Existente'
	variable2 = 'nomodifica_rut'
	paciente  =  Pacientes.objects.get(id=id) # registro en tabla
	form 	=  PacientesForm(request.POST,instance=paciente) # reg. en form
	var_fe_ini = paciente.fe_ini
	#return HttpResponse("viene con:"+str(paciente.nombre)+" "+str(var_fe_ini))
	#
	region  =  Param.objects.filter(tipo='REGI').order_by('descrip')
	comuna  =  Param.objects.filter(tipo='COMU').order_by('descrip')
	sexo    =  Param.objects.filter(tipo='SEXO').order_by('codigo')
	cob     =  Param.objects.filter(tipo='COBR').order_by('codigo')
	clasi   =  Param.objects.filter(tipo='PROC').order_by('codigo')
	abon    =  Param.objects.filter(tipo='ABON').order_by('codigo')
	yace	=  Param.objects.filter(tipo='YACE').order_by('-valor1')
	#
	if request.method == 'POST':
		if (form.is_valid()):
			form.save()
			return redirect('grid_pacientes')
		
	#despliega el template para modificacion
	form = PacientesForm(instance=paciente) # trae el registro completo
	var_region = paciente.region # entrega valor del campo de la tabla
	var_comuna = paciente.comuna # entrega valor del campo de la tabla
	chek_x     = paciente.estado
	var_sex    = paciente.sexo   # entrega valor del campo de la tabla
	var_cob    = paciente.cob	# tipo de cobranza
	var_clasi  = paciente.clasi
	var_abon   = paciente.abon #
	var_yace   = paciente.yace #Hosp,domicilio,clinica,MaAyuda
	var_doc_cobro = paciente.doc_cobro
	if paciente.doc_cobro == None:
		var_doc_cobro = "3"

	#return HttpResponse("Viene con :"+str(var_doc_cobro))
	context = {
			"variable1":variable1,
			"variable2":variable2,
			"form":form,
			"sexo":sexo,
			"region":region,
			"comuna":comuna,
			"yace":yace,
			"cob":cob,
			"clasi":clasi,
			"abon":abon,
			"var_sex":var_sex,
			"var_region":var_region,
			"var_comuna":var_comuna,
			"var_cob":var_cob,
			"var_clasi":var_clasi,
			"var_abon":var_abon,
			"var_yace":var_yace,
			"var_doc_cobro":var_doc_cobro,
			}
	return render(request,'ficha_pacientes.html',context)


def MenuParam(request):
	variable1 = 'Mantención de Parametros'
	logo = "/static/img/Logo_AsistenciaIntegral.jpeg"
	context ={ "variable1":variable1,"logo_corp":logo,}
	return render(request,'menuparametros.html',context)


def FichaParam(request,id):
	variable1 = 'Modificando Parametros del Sistema'
	param = Param.objects.get(id=id)
	#BOTON ACEPTAR en el template
	if request.method == "POST":
		form = ParamForm(request.POST,instance=param)
		if form.is_valid():
			form.save()
			return redirect('grid_param')
		else:
			#falló la actualizacion
			form = ParamForm(instance = param)
			context = {
				"variable1":variable1,
				"form":form,
				"id_x":id,
			}
			render(request,'ficha_param.html',context)
	else:
		# x GET - puebla el template.
		form = ParamForm(instance=param) # trae el formulario completo
		context = {
			"variable1":variable1,
			"form":form,
			"id_x":id,
			}
	return render(request,'ficha_param.html',context)


def no_esta(rut_x,lista):
    if rut_x in lista:
        return False
    return True
#

# LLAMADA DESDE PRINCIPAL.HTML
def grid_pauta(request):
	variable1 = 'Pauta Diaria'
	fechahoy = datetime.now() 
	dia_hoy  = fechahoy.day
	mes_hoy  = fechahoy.month
	ano_hoy  = fechahoy.year
	paciente = Pacientes.objects.filter(Q(estado=False))
	#
	fecha = str(ano_hoy)+"-"+str(mes_hoy).zfill(2)+"-"+str(dia_hoy)+" 00:00:00"
	#return HttpResponse("fecha para traer pauta :"+str(fecha))
	pauta = Pauta.objects.filter(fecha=fecha)
	#	     
	# Total dias del mes
	dias = []
	totdias = calendar.monthrange(ano_hoy,mes_hoy)[1] 
	for k in range(1,totdias+1):  # el rango superior lo excluye por eso el +1 
		dias.append(k)

	# El indice de los arreglos parten con cero		
	meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
	'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
	mes_hoy = meses[mes_hoy - 1]	# mes en palabras
	mes_numerico = fechahoy.month   # mes en numero

	# define 3 años para atras + uno adelante
	ano = [0,0,ano_hoy,0]
	ano[0] = ano_hoy -2
	ano[1] = ano_hoy - 1
	ano[3] = ano_hoy + 1
	
	# Agregando RUT's al arreglo		
	aPauta = []	
	for j in pauta:
		aPauta.append(j.rut)

	#inserta registro en ai_pauta
	fecha = str(ano_hoy)+"-"+str(mes_numerico).zfill(2)+"-"+str(dia_hoy).zfill(2)+" 00:00:00"
	fecha2 = "2019-11-02 00:00:00"
	#return HttpResponse("fecha insert, fecha y fecha2: "+str(fecha)+" "+str(fecha2))
	cursor = connection.cursor() #es necesario: from django.db import connection
	for k in paciente:
		if  not k.rut in aPauta:
			cursor.execute("insert into ai_pauta (rut,paciente,fecha,tipo_turno1,tipo_turno2,tipo_turno3) "
					"values(%s,%s,%s,%s,%s,%s)",[k.rut,k.nombre,fecha,'0','0','0'])
	cuenta = 0
	for ss in pauta:
		cuenta = cuenta + 1

	context = {
		"pauta":pauta,
		"variable1":variable1,
		"dias":dias,
		"meses":meses,
		"ano":ano,
		"dia_hoy":dia_hoy,
		"mes_hoy":mes_hoy,
		"ano_hoy":ano_hoy,
		"cuenta":cuenta,
		"mes_numerico":mes_numerico,}
	return render(request,'grid_pauta.html',context)


# BUSCA boton buscar
def grid_pautaBusca(request):
	variable1 = 'Pauta Diaria'
	buscar = request.GET.get('buscar').strip()  # desde el template x method='GET'
	dia_x  = request.GET.get('dias')  # desde el template x method='GET'
	mes_x  = request.GET.get('meses') # desde el template x method='GET'
	ano_x =  request.GET.get('ano')   # desde el template x method='GET'
	#   
	#pauta =  Pauta.objects.filter(Q(paciente__icontains=queryset) & Q(estado=False))
	fechahoy = datetime.now() 
	dia_hoy  = fechahoy.day
	mes_hoy  = fechahoy.month
	ano_hoy  = fechahoy.year
	#
	# llena arreglo con numeral de dias
	dias = []
	k=1
	for i in range(31):
		dias.append(k)
		k=k+1

	# El indice de los arreglos parten con cero		
	meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
	'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

	# define 3 años para atras + uno adelante
	ano = [0,0,ano_hoy,0]
	ano[0] = ano_hoy -2
	ano[1] = ano_hoy - 1
	ano[3] = ano_hoy + 1

	#preparar para busqueda
	dia_z = str(dia_x).zfill(2)  	# transforma a string y llena ceros izq.
	mes_z = meses.index(mes_x) + 1  # entrega el numerico del mes
	mes_z = str(mes_z).zfill(2)
	fecha = str(ano_x)+"-"+mes_z+"-"+dia_z+" 00:00:00"
	pauta =  Pauta.objects.filter(Q(paciente__icontains=buscar) & Q(fecha=fecha))

	cuenta = 0	# numero de pactes segun busqueda
	for ss in pauta:
		cuenta = cuenta + 1

	if cuenta == 0 :
		#return HttpResponse("cuenta :"+str(cuenta))
		grid_pauta(request)

	# numerico, asi lo requiere combo-box en grid_pauta	
	dia_hoy  = int(dia_x) 
	mes_hoy  = mes_x

	context = {
		"pauta":pauta,
		"variable1":variable1,
		"dias":dias,
		"meses":meses,
		"ano":ano,
		"dia_hoy":dia_hoy,
		"mes_hoy":mes_hoy,
		"ano_hoy":ano_hoy,
		"cuenta":cuenta,}
	return render(request,'grid_pauta.html',context)


# ACTUALIZA FICHA DE PAUTA
def ActualizaPauta(request,id):
	error1= "ok"
	variable1 = 'Definiendo / Actualizando Pauta'
	tipo_turno = ['-No asignado','Contratado','Extra']
	pauta   =  Pauta.objects.get(id=id)	# registro en tabla
	form 	=  PautaForm(request.POST,instance=pauta) # reg. en formulario HTML
	#
	turno1	=  Cuidadores.objects.all().order_by('nombre')
	turno2 	=  Cuidadores.objects.all().order_by('nombre')
	turno3 	=  Cuidadores.objects.all().order_by('nombre')
	yace	=  Param.objects.filter(tipo='YACE').order_by('descrip')
	rut_    =  pauta.rut   # rut paciente, registro en tabla
	paciente = Pacientes.objects.filter(rut=rut_) # solo el paciente del RUT
	
	var_rutcui1 = pauta.rut_t1
	var_rutcui2 = pauta.rut_t2
	var_rutcui3 = pauta.rut_t3
	#
	if request.method == 'POST':
		if (form.is_valid()):
			rut_t1 = request.POST.get('rut_t1') # contenido del template PAUTA
			rut_t2 = request.POST.get('rut_t2') # contenido template 
			rut_t3 = request.POST.get('rut_t3') # contenido template 
			#
			tipo_turno1 = request.POST.get('tipo_turno1')
			tipo_turno2 = request.POST.get('tipo_turno2')
			tipo_turno3 = request.POST.get('tipo_turno3')
			pauta.tipo_turno1 = tipo_turno1   # es tipo caracter
			pauta.tipo_turno2 = tipo_turno2   # es tipo caracter
			pauta.tipo_turno3 = tipo_turno3   # es tipo caracter
			#	
			# valores de variables asignadas a campos antes de grabar 
			for r in turno1:
				if r.rut == rut_t1:
		   			pauta.turno1 = r.nombre	
		   			pauta.valor_t1 = r.apago1

			for r in turno2:
				if r.rut == rut_t2:
		   			pauta.turno2 = r.nombre
		   			pauta.valor_t2 = r.apago2	

			for r in turno3:
				if r.rut == rut_t3:
		   			pauta.turno3 = r.nombre	
		   			pauta.valor_t3 = r.apago3

			form.save()
			return redirect('grid_pauta')
		else:
			return HttpResponse("Algo salió mal y no ha grabado"+str(form))
	#despliega el template para modificacion
	form = PautaForm(instance=pauta) # trae el registro completo
	var_yace = pauta.yace
	var_tip1 = tipo_turno[int(pauta.tipo_turno1)] #  obtiene la glosa del arreglo
	var_tip2 = tipo_turno[int(pauta.tipo_turno2)] #  obtiene la glosa del arreglo
	var_tip3 = tipo_turno[int(pauta.tipo_turno3)] #  obtiene la glosa del arreglo

	context = {
			"form":form,
			"variable1":variable1,
			"yace":yace,
			"var_yace":var_yace,
			"turno1":turno1,
			"turno2":turno2,
			"turno3":turno3,
			"var_rutcui1":var_rutcui1,
			"var_rutcui2":var_rutcui2,
			"var_rutcui3":var_rutcui3,
			"var_tip1":var_tip1,
			"var_tip2":var_tip2,
			"var_tip3":var_tip3,
			"tipo_turno":tipo_turno,
			}
	return render(request,'ficha_pauta.html',context)


def is_int(s):
    try:
        return int(s)
    except ValueError:
        return False

def	valida_tipoturno():
	if request.POST.get('tipo_turno1') == '0':
		return False

	