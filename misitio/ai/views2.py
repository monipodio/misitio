#  nuevo views2
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from misitio.ai.forms import CuidadoresForm
from misitio.ai.forms import ApoderadosForm
from misitio.ai.forms import PacientesForm
from misitio.ai.forms import ParamForm
from misitio.ai.forms import PautaForm
from misitio.ai.forms import ResupautaForm
from misitio.ai.forms import DetapautaForm
from misitio.ai.forms import AnticiposForm
from misitio.ai.forms import Pauta_auxForm
from misitio.ai.forms import Pacientes_auxForm
from misitio.ai.models import Cuidadores,Pacientes,Apoderados,Detapauta
from misitio.ai.models import Param,Pauta,Resupauta
from misitio.ai.models import Anticipos,Pauta_aux,Pagocui_aux
from misitio.ai.models import Pacientes_aux 
from misitio.ai.models import Mensual_aux 
from misitio.ai.models import Diario_aux,Saldos 
from misitio.ai.misfunciones import anticipos,preparadia,boleta,saldoant,fecha_actual 
from misitio.ai.misfunciones import nombrearch,fecha_palabra,nturnos,grabasaldo
from misitio.ai.misfunciones import edad,fecha_ddmmaaaa

from django.shortcuts import get_list_or_404, get_object_or_404

from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
import os, sys,shutil
from os import remove
from os import scandir, getcwd,startfile
from datetime import datetime,timedelta,date
from django.db import DatabaseError, transaction
from django.db import connection
import calendar

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side
from openpyxl.styles import colors
from openpyxl.styles import Font, Color,Fill
from openpyxl.styles.borders import BORDER_THIN
from openpyxl.drawing.image import Image as XLIMG

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image

from reportlab.lib import colors
from reportlab.lib.colors import blue,white,black
from reportlab.lib.units import inch, mm 
from reportlab.platypus import Paragraph 
from reportlab.lib.styles import ParagraphStyle 
from reportlab.lib.enums import TA_CENTER 
from reportlab.platypus.tables import TableStyle, Table
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib import styles
from io import BytesIO
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont

from tabulate import tabulate

import wget
from PIL import Image
from django.http import FileResponse, Http404
import getpass
from getpass import getuser
from misitio.ai.forms import UploadFileForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from reportlab.platypus.flowables import Flowable
from reportlab.lib.styles import getSampleStyleSheet
#

@login_required(login_url='login_ini')
def gestionremota2(request):
	fechahoy = datetime.now()
	ancho, alto = letter	# alto=792,ancho=612 - posicion normal	
	nom_arch = "gestionre2"+nombrearch()+".pdf"  # gestion remota
	#
	# desarrollo
	logo_corp = os.getcwd()+"\\misitio\\ai\\static\\img\\Logo_AsistenciaIntegral.jpg"
	c = canvas.Canvas(os.getcwd() +"\\pdfs\\"+ nom_arch, pagesize=letter)
	#
	#produccion
	#logo_corp = os.getcwd()+"/misitio/staticfiles/img/Logo_AsistenciaIntegral.jpg"
	#c = canvas.Canvas(os.getcwd() +"/misitio/pdfs/"+ nom_arch, pagesize=letter)
	#
	c.setPageSize((ancho, alto))
	#
	rut_aux = request.session['rut_x']		
	paciente  =  Pacientes.objects.get(rut=rut_aux) 

	if paciente.fe_ini == None:
		return HttpResponse("Paciente no posee fecha de inicio")

	# produccion
	#path_x = os.getcwd() +"/misitio/pdfs/"

	# Desarrollo
	path_x = os.getcwd() +'\\pdfs\\'

	arch_y = os.listdir(path_x)
	for arch_pdf in arch_y:
		remove(path_x+arch_pdf)
	#	
    ## ####comienza primera pagina ##############################
	y = 710
	c.drawImage(logo_corp, 10, y,190,80) # (IMAGEN, X,Y, ANCHO, ALTO)
	y = 700
	c.setFont('Helvetica-Bold', 11)
	c.drawString(190,y, "GESTION REMOTA DE PACIENTES CIMAS + D")
	c.setFont('Helvetica', 11)
	#
	# subrrayado de "GESTION REMOTA DE PACIENTES"
	y=y-20
	c.line(190, y+16, 436, y+16) # x,y,z,w en donde x=posic. horiz. inicial,y=poc.inicial verical,w=poc.vert.final
	#
	c.setFont('Helvetica-Bold', 10)
	y = y - 20
	c.drawString(50,y,"NOMBRE: "+str(paciente.nombre)+"      R.U.T.:"+rut_aux)
	y = y - 20	
	c.drawString(50,y,"FECHA: "+"_______/_________/__________")
	y = y - 30	
	c.drawString(50,y,"MOTIVO POR EL QUE SE REALIZA: ________________________________")

	y = y - 30	
	c.drawString(50,y,"2.-EVALUACION COGNITIVA:")
	#
	c.setFont('Helvetica', 10)
	y=y-20
	# rectangulo
	c.rect(50, y-7, 510, 17)
	c.drawString(53,y,"Test Memoria Acortado - SPMSQ -  E. PFEIFER 1975")
	y=y-15
	# rectangulo	
	c.rect(50, y-9, 510, 17)
	c.drawString(53,y-3,"EVALUABLE:______________ NOEVALUABLE:_________________")
	y=y-25
	c.drawString(50,y,"Pregunte desde el número 1 al 10, y complete las respuestas. Pregunte el número 4 A solo si el paciente no ")
	y=y-15
	c.drawString(50,y,"tiene telefono. Anote al final el número de errores.")
	#
	y=y-32
	c.drawString(50,y,"Se acepta UN ERROR MAS, si tiene educación basica o ninguna")
	y=y-25
	c.drawString(50,y,"Se acepta UN ERROR MENOS, si tiene educación superior")
	#
	### COMIENZA DEFINICION GRID
	data = [
		["Bueno","Malo","Pregunta"],
		["","","¿Que fecha es hoy? (dia-mes-año)"],
		["","","¿ Que dia de la semana es hoy ?"], 
		["","","¿Cual es el nombre de este lugar o edificio?"],
		["","","¿Cual es su número de telefono? 4A ¿Cual es su dirección ?(solo si no tiene telefono)"],
		["","","¿Que edad tien usted?"],
		["","","¿En que fecha nacio? (dia-mes-año)"],
		["","","¿Cual es el presidente de Chile Actualmente?"],
		["","","¿Cual fue el presidente anterior?"],
		["","","¿Cual es el appellido de su madre?"],
		["","","A 20, restale 3, y continue restandole 3 a cada resultado hasta el final (20-17-14-11-8-5-2)"],
	]

	# definicion de cada columna (primera grid)
	t = Table(data, colWidths=[43,43,420])	

	t.setStyle(TableStyle([
		("ALIGN", (0, 0), (-1, -1), "LEFT"),
		("ALIGN", (-2, 1), (-2, -1), "LEFT"),
		("GRID", (0, 0), (-1, -1), 0.25, colors.black),
		("BOX", (0, 0), (-1, -1), 0.25, colors.black),
		("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
	]))
	w, h = t.wrap(100, 100)   # OBLIGAORIO
	t.drawOn(c, 50, 220, 0)   # DIBUJA LA GRID EN MEMORIA
	# FIN DE DEFINICION DE LA GRID

	# rectangulo
	y=130
	c.roundRect(50, y, 506, 91, 4, stroke=1, fill=0)

	c.drawString(53,y+68,"Total") 
	c.drawString(142,y+68,"0-2 errores: Funciones intelectuales intactas")
	y=178
	c.drawString(142,y,"3-4 errores: Deterioro intelectual leve")
	y=y-20
	c.drawString(142,y,"5-7 errores: Deterioro intelectual moderado")
	y=y-20
	c.drawString(142,y,"8-10 errores: Deterioro intelectual severo")
	#
	c.setFont('Helvetica-Bold', 10)
	y=y-30
	c.drawString(50,y,"Observaciones:")
	c.setFont('Helvetica', 10)
	y=y-30
	c.line(50, y+16, 556, y+16) # x,y,z,w en donde x=posic. horiz. inicial,y=poc.inicial verical,w=poc.vert.final
	y=y-30
	c.line(50, y+16, 556, y+16) # x,y,z,w en donde x=posic. horiz. inicial,y=poc.inicial verical,w=poc.vert.final
	y=y-30
	c.line(50, y+16, 556, y+16) # x,y,z,w en donde x=posic. horiz. inicial,y=poc.inicial verical,w=poc.vert.final

	## ########  FIN DEL REPORTE ####################
	c.showPage() #salto de pagina
	c.save()  #Archivamos y cerramos el canvas
	#Lanzamos el pdf creado
	os.system(nom_arch)

	#desarrollo
	return FileResponse(open(os.getcwd() +'\\pdfs\\'+ nom_arch,'rb'), content_type='application/pdf')


@login_required(login_url='login_ini')
def ingresopaciente(request):
	fechahoy = datetime.now()
	ancho, alto = letter	# alto=792,ancho=612 - posicion normal	
	nom_arch = "infoingreso"+nombrearch()+".pdf"  # gestion remota
	#
	# desarrollo
	logo_corp = os.getcwd()+"\\misitio\\ai\\static\\img\\Logo_AsistenciaIntegral.jpg"
	c = canvas.Canvas(os.getcwd() +"\\pdfs\\"+ nom_arch, pagesize=letter)
	#
	#produccion
	#logo_corp = os.getcwd()+"/misitio/staticfiles/img/Logo_AsistenciaIntegral.jpg"
	#c = canvas.Canvas(os.getcwd() +"/misitio/pdfs/"+ nom_arch, pagesize=letter)
	#
	c.setPageSize((ancho, alto))
	#
	rut_aux = request.session['rut_x']		
	paciente  =  Pacientes.objects.get(rut=rut_aux) 

	if paciente.fe_ini == None:
		return HttpResponse("Paciente no posee fecha de inicio")

	fe_nac = paciente.fe_nac
	edad_x = edad(paciente.fe_nac) # en misfunciones.py
	sexo_x = "Masculino"
	if paciente.sexo == 2:
		sexo_x = "Femenino"  

	domicilio_x = paciente.direccion	
	fono_pcte   = paciente.fono_pcte
	fe_nac      = paciente.fe_nac

	region_x = "(sin definir)"
	region  =  Param.objects.filter(tipo='REGI',codigo=paciente.region)
	for re in region:
		region_x = re.descrip

	comuna_x = "(sin definir)"	
	comuna  =  Param.objects.filter(tipo='COMU',codigo=paciente.comuna)
	for co in comuna:
		comuna_x = co.descrip
  
	# produccion
	#path_x = os.getcwd() +"/misitio/pdfs/"

	# Desarrollo
	path_x = os.getcwd() +'\\pdfs\\'

	arch_y = os.listdir(path_x)
	for arch_pdf in arch_y:
		remove(path_x+arch_pdf)
	#	
    ## ####comienza primera pagina ##############################
	y = 710
	c.drawImage(logo_corp, 25, y,190,80) # (IMAGEN, X,Y, ANCHO, ALTO)
	y = 700
	c.setFont('Helvetica-Bold', 11)
	c.drawString(198,y, "INFORME INGRESO PACIENTE")
	c.setFont('Helvetica', 11)
	# subrrayado de "informe ingreso paciente"	
	y=y-20
	c.line(197, y+16, 361, y+16) # x,y,z,w en donde x=posic. horiz. inicial,y=poc.inicial verical,w=poc.vert.final
	#
	#
	y=y-10	
	c.drawString(420,y,"Fecha:_____/_____/______")	
	#
	y = y - 30	

	# DEFINICION DE PRIMERA GRID ###################################
	c.setFont('Helvetica-Bold', 10)
	c.drawString(50,620,"Datos del paciente")
	c.setFont('Helvetica', 10)
	y=y-15

	data = [
		["Nombre completo",paciente.nombre],
		["RUT",paciente.rut],
		["Fecha de nacimiento",fecha_ddmmaaaa(fe_nac)], 
		["Edad",edad(fe_nac)],
		["Sexo",sexo_x],
		["Dirección",paciente.direccion],
		["Comuna",comuna_x],
		["Región",region_x],
		["Telofono",paciente.fono_pcte],
		["Apoderado del paciente",paciente.n_apod],
		["Teléfono del apoderado del paciente",paciente.f_apod],
		["Personas que vive en el domicilio y parentesco",""],
	]

	# definicion de cada columna (primera grid)
	t = Table(data, colWidths=[230,280])	

	t.setStyle(TableStyle([
		("ALIGN", (0, 0), (-1, -1), "LEFT"),
		("ALIGN", (-2, 1), (-2, -1), "LEFT"),
		("GRID", (0, 0), (-1, -1), 0.25, colors.black),
		("BOX", (0, 0), (-1, -1), 0.25, colors.black),
		("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
	]))
	w, h = t.wrap(100, 100)   # OBLIGAORIO
	t.drawOn(c, 50, 390, 0)   # DIBUJA LA GRID EN MEMORIA
	# FIN DE DEFINICION DE PRIMERA GRID
	#
	#
	#
    # INICIA DEFINICION DE SEGUNDA GRID ################################
	y = 365	
	c.setFont('Helvetica-Bold', 10)
	c.drawString(50,y,"Datos de la empresa de cuidados domiciliarios:")
	c.setFont('Helvetica', 10)
	y=y-15
    #
	data = [

		["Nombre empresa",""],
		["Nombre enfermera",""],
		["Telefono enfermera o coordinador de la empresa",""], 
	]

	# Definicion de cada columna (segunda grid)
	t = Table(data, colWidths=[230,280])	

	t.setStyle(TableStyle([
		("ALIGN", (0, 0), (-1, -1), "LEFT"),
		("ALIGN", (-2, 1), (-2, -1), "LEFT"),
		("GRID", (0, 0), (-1, -1), 0.25, colors.black),
		("BOX", (0, 0), (-1, -1), 0.25, colors.black),
		("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
	]))
	w, h = t.wrap(100, 100)   # OBLIGAORIO
	t.drawOn(c, 50, 300, 0)   # DIBUJA LA GRID EN MEMORIA


    # INICIA DEFINICION DE TERCERA GRID ################################
	y = 275	
	c.setFont('Helvetica-Bold', 10)
	c.drawString(50,y,"Datos contacto:")
	c.setFont('Helvetica', 10)
	y=y-15
    #
	data = [

		["Contacto",""],
		["Fono contacto",""], 
		["",""], 
	]

	# Definicion de cada columna (tercera grid)
	t = Table(data, colWidths=[230,280])	

	t.setStyle(TableStyle([
		("ALIGN", (0, 0), (-1, -1), "LEFT"),
		("ALIGN", (-2, 1), (-2, -1), "LEFT"),
		("GRID", (0, 0), (-1, -1), 0.25, colors.black),
		("BOX", (0, 0), (-1, -1), 0.25, colors.black),
		("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
	]))
	w, h = t.wrap(100, 100)   # OBLIGAORIO
	t.drawOn(c, 50, 210, 0)   # posiciona y DIBUJA LA GRID EN MEMORIA

   # INICIA DEFINICION DE CUARTA GRID ################################
	y = 190
	c.setFont('Helvetica-Bold', 10)
	c.drawString(50,y,"Datos de accidente:")
	c.setFont('Helvetica', 10)
	y=y-15
    #
	data = [

		["Contacto",""],
		["Fono contacto",""], 
		["",""], 
	]

	# Definicion de cada columna (cuarta grid)
	t = Table(data, colWidths=[230,280])	

	t.setStyle(TableStyle([
		("ALIGN", (0, 0), (-1, -1), "LEFT"),
		("ALIGN", (-2, 1), (-2, -1), "LEFT"),
		("GRID", (0, 0), (-1, -1), 0.25, colors.black),
		("BOX", (0, 0), (-1, -1), 0.25, colors.black),
		("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
	]))
	w, h = t.wrap(100, 100)   # OBLIGAORIO
	t.drawOn(c, 50, 125, 0)   # posiciona y DIBUJA LA GRID EN MEMORIA
	#
	##### INICIA CAJA DE COMENTARIOS #############################
	c.setFont('Helvetica-Bold', 10)
	c.drawString(50,105,"Comentarios de ingreso:")
	c.setFont('Helvetica', 10)

	# rectangulo
	c.rect(50,50 ,510,47)


	## ########  FIN DEL REPORTE ####################
	c.showPage() #salto de pagina
	c.save()  #Archivamos y cerramos el canvas
	#Lanzamos el pdf creado
	os.system(nom_arch)

	#desarrollo
	return FileResponse(open(os.getcwd() +'\\pdfs\\'+ nom_arch,'rb'), content_type='application/pdf')




@login_required(login_url='login_ini')
def georeferencia(request):
	variable1 = 'Geo-referencia'
	rut_aux = request.session.get('rut_x') # rescata variable global  
	paciente  =  Pacientes.objects.get(rut=rut_aux) # busca
	paciente_id = paciente.id
	coordenadas = paciente.coordenadas
	localizacion = paciente.localizacion

	if coordenadas == None:
		return HttpResponse("Ficha no posee coordenadas de georeferenciación")
		return redirect('ActualizaPac',paciente_id) # ficha paciente

	lat = coordenadas[0:10]
	lng = coordenadas[12:22]
	context = {
		'variable1':variable1,
		'paciente_id':paciente_id,
		'variable3':paciente.nombre,
		'lat':lat,
		'lng':lng,
		'localizacion':localizacion,
	}	
	#return render(request,'georeferencia.html',context)
	return render(request,'ejemplo_georeferencia.html',context)

