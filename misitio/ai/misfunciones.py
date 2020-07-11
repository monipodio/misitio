#from django.test import TestCase
from django.http import HttpResponse, HttpResponseRedirect
import sys
from django.urls import path
from django.db import connection,transaction
from django import forms
from misitio.ai.models import Anticipos,Pauta,Saldos,Pacientes
#
from datetime import datetime
from datetime import timedelta,date
import calendar
# #####################

def anticipos(rut_x,fe_i,fe_f):
	fecha_ini = fe_i
	fecha_fin = fe_f
	anticipo = Anticipos.objects.filter(rut=rut_x,fecha__range=(fecha_ini, fecha_fin)).order_by('fecha')
	tot_anti = 0
	for anti in anticipo:
		tot_anti = tot_anti + anti.valor 
	return tot_anti	

def boleta(rut_x,fe_i,fe_f):
	fecha_ini = fe_i
	fecha_fin = fe_f
	anticipo = Anticipos.objects.filter(rut=rut_x,fecha__range=(fecha_ini, fecha_fin)).order_by('fecha')
	bole = 0
	for bole in anticipo:
		bole = bole.boleta 
	return bole	

def nombrearch():
	fechahoy = datetime.now()
	segundo_x = str(fechahoy.second).zfill(2)
	minuto_x = str(fechahoy.minute).zfill(2)
	hora_x = str(fechahoy.hour).zfill(2)
	dia_x = str(fechahoy.day).zfill(2)	   # dia en numero-caracter
	mes_x = str(fechahoy.month).zfill(2)   # mes en numero-caracter
	ano_x = str(fechahoy.year)
	string_nombre = ano_x+mes_x+dia_x+hora_x+minuto_x+segundo_x
	return string_nombre

def fecha_actual():
	# entrega dd-mm-aaaa como string
	fechaactual = datetime.now() 
	dia_actual =  fechaactual.day
	ano_actual  = fechaactual.year
	mes_actual  = fechaactual.month
	return str(dia_actual).zfill(2)+"-"+str(mes_actual).zfill(2)+"-"+str(ano_actual)

def fecha_ddmmaaaa(fecha_x):
	# entrega dd-mm-aaaa de fecha_x
	if fecha_x == None:
		dia_ac = 0
		mes_ac = 0
		ano_ac = '0000'
	else:
		dia_ac  = fecha_x.day
		ano_ac  = fecha_x.year
		mes_ac  = fecha_x.month
	return str(dia_ac).zfill(2)+"-"+str(mes_ac).zfill(2)+"-"+str(ano_ac)

def fecha_aaaammdd(fecha_x):
	# entrega dd-mm-aaaa como string
	fechaactual = fecha_x 
	#dia_actual =  fechaactual.day
	#ano_actual  = fechaactual.year
	#mes_actual  = fechaactual.month
	return str(fecha_x)[0:3]+"-"+str(fecha_x).zfill(2)+"-"+str(fecha_x).zfill(2)


def fecha_palabra(fe_x):
	#9999-99-99
	fe_x = str(fe_x)
	meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
	'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']	
	dia_x = fe_x[8:10] # sintaxis: arreglo[inicio:final-1]
	mes_x = fe_x[5:7]
	mes_x = meses[int(mes_x) - 1]	# mes en palabras
	ano_x = fe_x[0:4]
	fecha_pala = mes_x+" "+dia_x+" de "+ano_x
	return fecha_pala

def nturnos(rut_x,fe_i,fe_f):
	lista_uno = []
	tot_turnos = 0
	tot_valmes = 0
	turnos = Pauta.objects.filter(rut=rut_x,fecha__range=(fe_i, fe_f))
	#abonos_x = anticipos(rut_x,fe_i,fe_f)
	for tur in turnos:
		if tur.turno1 != None:
			if len(tur.turno1) != 0:	
				tot_turnos = tot_turnos + 1
				if tur.valor_p1 != None:
					tot_valmes = tot_valmes + tur.valor_p1	
				
		if tur.turno2 != None:
			if len(tur.turno2) != 0:	
				tot_turnos = tot_turnos + 1
				if tur.valor_p2 != 0:
					tot_valmes = tot_valmes + tur.valor_p2

		if tur.turno3 != None:
			if len(tur.turno3) != 0:
				tot_turnos = tot_turnos + 1
				if tur.valor_p3 != 0:
					tot_valmes = tot_valmes + tur.valor_p3

	#return [tot_turnos,tot_valmes,abonos_x]
	return [tot_turnos,tot_valmes]

def preparadia(rut_x,mes_numerico,ano_hoy,totdias,paciente_x,usuario_y):
	ldias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
	cursor = connection.cursor() # es necesario: from django.db import connection
	primerdia_delmes = calendar.monthrange(ano_hoy,mes_numerico)[0]
	ndia = primerdia_delmes - 1		# primerdia_delmes entrega 2 
	k=1
	puntero_dia = primerdia_delmes  

	# Prepara el mes con detalle 
	while k <= totdias:
		ndia = k #ndia + 1	
		cdia = ldias[puntero_dia] # glosa del dia que corresponde.
		fecha_x = str(ano_hoy)+"-"+str(mes_numerico).zfill(2)+"-"+str(k).zfill(2)+" 00:00:00"

		cursor.execute(
			"insert into ai_diario_aux (rut,paciente,ndia,cdia,turno1,turno2,turno3,valor_t1,valor_t2,valor_t3,val_tot,acum1,abonos,acum2,fecha,username)"
		"values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		,[rut_x,paciente_x,ndia,cdia,0,0,0,0,0,0,0,0,0,0,fecha_x,usuario_y]
		)

		# Sin ceros 
		#cursor.execute(
		#	"insert into ai_diario_aux (rut,paciente,ndia,cdia,fecha)"
		#"values(%s,%s,%s,%s,%s)"
		#,[rut_x,paciente_x,ndia,cdia,fecha_x]
		#)

		puntero_dia = puntero_dia + 1
		if puntero_dia == 7:
			puntero_dia = 0			
		k=k+1
	cursor.close()	
	return True	

def grabasaldo(nombre_x,rut_x,saldo_x,mes_x,ano_x):
	fechahoy = datetime.now()	
	# Verifica que el registro de saldo existe
	existe_x = Saldos.objects.filter(rut=rut_x,mes=mes_x,ano=ano_x).exists()
	if existe_x == False:	# solo registro inexistente en registro de SALDOS
		# Detecta el ultimo saldo historico de este rut para incorporarlo al actual periodo
		sa= 0
		sald_ant = Saldos.objects.filter(rut=rut_x).order_by('fecha')
		for s in sald_ant:
			sa = s.saldo

		cursor = connection.cursor() # es necesario: from django.db import connection
		cursor.execute(
		"insert into ai_saldos (nombre,rut,mes,ano,saldoant,saldo,fecha)"
		"values(%s,%s,%s,%s,%s,%s,%s)"
		,[nombre_x,rut_x,mes_x,ano_x,sa,sa,fechahoy]
		)
	else:
		# Actualiza el saldo y fecha
		cursor = connection.cursor() 
		cursor.execute(
			"update ai_saldos set saldo = %s,fecha=%s"
			" where rut = %s and mes = %s and ano = %s"
			,[saldo_x,fechahoy,rut_x,mes_x,ano_x])
	return True


# Lee saldo anterior
def saldoant(rut_x,mes_x,ano_x):
	mes_x  = mes_x - 1	 # 11-04-2020
	if mes_x == 1: # 11-04-2020
		mes_x = 12	# 11-04-2020
		ano_x = ano_x - 1 # 11-04-2020
	sal_x = Saldos.objects.filter(rut=rut_x,mes=mes_x,ano=ano_x)
	saldo_ant = 0
	for s in sal_x:
		saldo_ant = s.saldo
		if s.saldoant == None:
			saldo_ant = 0	
	return saldo_ant	


def ayuda1():
	alert("La forma de poner fotos a una FICHA DE CUIDADOR es de la siguiente manera:");
	return True

#def abrepdf(archpdf):
#	webbrowser.open_new_tab("c:\carpeta_django\misitio\pdfs\contrato20200217225333.pdf")	
#	return True

def edad(fe_nac):
	today = datetime.now()
	if fe_nac == None:
		edad_x = 0
	else:	 
		dia_fe_nac =  fe_nac.day
		mes_fe_nac  = fe_nac.month
		ano_fe_nac  = fe_nac.year
		birth_date = datetime(ano_fe_nac, mes_fe_nac, dia_fe_nac)
		rectifier = datetime(today.year, birth_date.month, birth_date.day) >= today
		edad_x = ('{}'.format(today.year - birth_date.year - rectifier))
	return edad_x


