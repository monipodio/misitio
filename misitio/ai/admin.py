# Register your models here.
# Aqui se registran los modelos que uno quiere que se administren con el 
# Django-Admin (GAG), ademas se definen las columnas que apareceran. 

from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Pacientes
from .models import Param
from .models import Cuidadores
from .models import Pauta

#titulo principal del panel Admin
admin.site.site_header = 'Administracion sistema: Asistencia Integral'

class AdminPacientes(admin.ModelAdmin):
	list_display = ["nombre","rut","fe_ini","n_apod"]
	menu_label = "Pacientes de AI"
	search_fields = ['nombre', 'n_apod']

class AdminParametros(admin.ModelAdmin):
	list_display = ["tipo","codigo","descrip","valor1","valor2",
	"sw_1","sw_2","fecha","corr"]
	search_fields = ['tipo', 'descrip']


class AdminCuidadores(admin.ModelAdmin):
	list_display = ["nombre","rut","direccion","fono_cuid","fono2_cuid","correo"]
	search_fields = ['nombre', 'direccion']

class AdminPauta(admin.ModelAdmin):
	list_display = ["fe_ini","paciente","rut","rut_t1",
	"turno1","rut_t2","turno2","rut_t3","turno3"]
	search_fields = ['fe_ini', 'paciente']


admin.site.register(Pacientes,AdminPacientes)
admin.site.register(Param,AdminParametros)
#admin.site.register(Apoderados,AdminApoderados)
admin.site.register(Cuidadores,AdminCuidadores)
admin.site.register(Pauta,AdminPauta)
