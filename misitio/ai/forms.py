from django import forms
from aintegral.ai.models import Cuidadores,Pacientes,Apoderados,Param
from datetime import datetime

class ParamForm(forms.ModelForm):
	class Meta:
		model = Param
		fields = "__all__" 

		def __str__(self):
			return self.descrip

class PacientesForm(forms.ModelForm):
	class Meta:
		model = Pacientes
		widgets = {
			'fe_ini': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		   	'fe_nac': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}

		fields = "__all__" 
		def __str__(self):
			return self.nombre


class CuidadoresForm(forms.ModelForm):
	class Meta:
		model = Cuidadores
		widgets = {
			'fe_ini': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		   	'fe_nac': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.nombre

class ApoderadosForm(forms.ModelForm):
	class Meta:
		model = Apoderados
		widgets = {
			'fe_ini': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.nombre

#class DateInput(forms.DateInput):
#	input_type = 'date'


