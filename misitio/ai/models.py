from django.db import models
from .models import *
from django.contrib import admin 
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage


my_store = FileSystemStorage(location='static/img/fotos')

class Pacientes(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80,verbose_name="Nombre Paciente")
    fe_ini = models.DateTimeField(blank=True, null=True,verbose_name="Fecha de Inicio")
    direccion = models.CharField(max_length=61)
    comuna= models.CharField(max_length=5)   
    region = models.CharField(max_length=2)
    fono_pcte = models.CharField(max_length=12, blank=True, verbose_name ='Fono del Paciente')
    fono2_pcte = models.CharField(max_length=12, blank=True, verbose_name ='Fono alternativo del Paciente')    
    fe_nac = models.DateTimeField(blank=True, null=True)
    sexo =  models.CharField(max_length=1,default=3)
    correo = models.CharField(max_length=40, blank=True)
    n_apod = models.CharField(max_length=80,verbose_name="Nombre Apoderado")
    rut_apod = models.CharField(max_length=10)
    dir_apod = models.CharField(max_length=61, blank=True,null=True)
    f_apod   = models.CharField(max_length=12, blank=True,null=True)
    fono2_apod = models.CharField(max_length=12, blank=True,null=True)
    parentes = models.CharField(max_length=30, blank=True,null=True)
    correo_apod = models.CharField(max_length=40, blank=True,null=True)
    medico = models.CharField(max_length=60, blank=True)
    notas = models.TextField(blank=True)
    cob =  models.CharField(max_length=1, null=True)
    estado = models.BooleanField(blank=True,default=0)  # pasivo - Activo
    clasi = models.CharField(max_length=1, blank=True, default='') # particular, institucion
    abon  = models.CharField(max_length=1, blank=True) # Efec,Cheq,Tarjeta,...
    yace = models.CharField(max_length=1, blank=True,null=True) # Hosp, dimiclio, Ma Ayuda, cli,,etc
    valor_t1 =  models.IntegerField(blank=True,default=0)
    valor_t2 =  models.IntegerField(blank=True,default=0)
    valor_t3 =  models.IntegerField(blank=True,default=0)
    doc_cobro = models.CharField(max_length=1, blank=True,null=True)

    def __str__(self):
        return self.nombre.strip() 
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Paciente'
  

class Cuidadores(models.Model):
    TIPO_CONTRATO = [('1', 'Contratado'),('2', 'Honorarios')]
    rut = models.CharField(max_length=10, blank=False)
    nombre = models.CharField(max_length=80, blank=True)
    fe_ini = models.DateTimeField(blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True)
    comuna= models.CharField(max_length=5, blank=True)   
    region = models.CharField(max_length=2, blank=True)
    fono_cuid = models.CharField(max_length=12, blank=True, verbose_name ='Fono Cuidador')
    fono2_cuid = models.CharField(max_length=12, blank=True, verbose_name ='Fono2 Cuidador')
    fe_nac = models.DateTimeField(blank=True, null=True)
    sexo =  models.CharField(max_length=1,blank=True)
    correo = models.CharField(max_length=40, blank=True)
    notas = models.TextField(blank=True)
    tipo =  models.CharField(max_length=1, blank=True) #contratado - honorarios 
    media = models.FileField(upload_to='fotos/',blank=True,default='') #si no existe, la crea
    clasi  = models.CharField(max_length=1, blank=True,default='') # superior-intermedio-Stand
    extran = models.CharField(max_length=1,blank=True,default='0')  # si es extrajero
    estado = models.BooleanField(blank=True,default=0)  # Activo - Pasivo
    instr  = models.CharField(max_length=1, blank=True) # nivel educacional
    elim_foto =  models.CharField(max_length=1, blank=True)  # switch para borrar archivo foto
    apago1  = models.IntegerField(blank=True,default=0) # salario
    apago2  = models.IntegerField(blank=True,default=0) # salario
    apago3  = models.IntegerField(blank=True,default=0) # salario

    def __str__(self):
        return self.nombre 
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Cuidadore'    


class Apoderados(models.Model):
    rut = models.CharField(max_length=10, blank=False)
    nombre = models.CharField(max_length=80, blank=True)
    direccion = models.CharField(max_length=60, blank=True)
    comuna= models.CharField(max_length=5, blank=True)   
    region = models.CharField(max_length=2, blank=True)
    fono_apod = models.CharField(max_length=12, blank=True, verbose_name ='Fono Cuidador')
    fono2_apod = models.CharField(max_length=12, blank=True, verbose_name ='Fono2 Cuidador')
    parentezco = models.CharField(max_length=50, blank=True)
    correo = models.CharField(max_length=40, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre 
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Apoderado'     

class Param(models.Model):
    tipo = models.CharField(max_length=5, blank=False)
    codigo = models.CharField(max_length=5, blank=True)
    descrip = models.CharField(max_length=79, null=True, verbose_name ='Desripcion')
    valor1 =  models.IntegerField(blank=True)
    valor2 =  models.IntegerField(blank=True)
    valor3 =  models.IntegerField(blank=True)
    sw_1   =  models.IntegerField(blank=True)
    sw_2   =  models.IntegerField(blank=True)
    notas  =  models.TextField(blank=True)
    fecha  =  models.DateTimeField(blank=True, null=True)
    corr   =  models.IntegerField(blank=True)
    fecha2 =  models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.descrip.strip() 
    
    class Meta:
        ordering = ['tipo','descrip']
        verbose_name = 'Parametro'

class Pauta(models.Model):
    rut = models.CharField(max_length=10,blank=True)
    paciente = models.CharField(max_length=80,verbose_name="Nombre Paciente",null=True)
    fe_ini = models.DateTimeField(blank=True,verbose_name="Fecha de Inicio")
    fecha  = models.DateTimeField(blank=True,verbose_name="Fecha Pauta")
    rut_t1 = models.CharField(max_length=10,blank=True)
    turno1 = models.CharField(max_length=80,verbose_name="Nombre turno1",blank=True)
    rut_t2 = models.CharField(max_length=10,blank=True)
    turno2 = models.CharField(max_length=80,verbose_name="Nombre turno1",blank=True)
    rut_t3 = models.CharField(max_length=10,blank=True)
    turno3 = models.CharField(max_length=80,verbose_name="Nombre turno1",blank=True)
    valor_t1 = models.IntegerField(blank=True)
    valor_t2 = models.IntegerField(blank=True)
    valor_t3 = models.IntegerField(blank=True)
    notas = models.TextField(blank=True)
    yace = models.CharField(max_length=1, blank=True,null=True) # Hosp, dimiclio, Ma Ayuda, cli,etc 
    tipo_turno1= models.CharField(max_length=1, blank=True,null=True) #
    tipo_turno2= models.CharField(max_length=1, blank=True,null=True) #
    tipo_turno3 = models.CharField(max_length=1, blank=True,null=True) #
    def __str__(self):
        return self.paciente.strip()
    
    class Meta:
        ordering = ['paciente']
        verbose_name = 'Pauta'
