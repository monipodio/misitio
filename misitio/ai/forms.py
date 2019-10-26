from django import forms
from misitio.ai.models import Cuidadores,Pacientes,Apoderados,Param,Pauta
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

class PautaForm(forms.ModelForm):
	class Meta:
		model = Pauta
		widgets = {
			'fe_ini': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.paciente


