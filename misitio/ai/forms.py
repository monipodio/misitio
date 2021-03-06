from django import forms
from misitio.ai.models import Cuidadores,Pacientes,Apoderados,Param,Pauta,Resupauta,Detapauta
from misitio.ai.models import Anticipos,Pauta_aux,Pacientes_aux,Diario_aux,Receta,Maefarm
from datetime import datetime
from django import forms

from django.forms import ModelForm, ClearableFileInput
from .models import UploadFile

class ParamForm(forms.ModelForm):
	class Meta:
		model = Param
		fields = "__all__" 

		def __str__(self):
			return self.descrip

class PacientesForm(forms.ModelForm):
	class Meta:
		model = Pacientes

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

class Pauta_auxForm(forms.ModelForm):
	class Meta:
		model = Pauta_aux
		widgets = {
			'fe_ini': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.paciente


class ResupautaForm(forms.ModelForm):
	class Meta:
		model = Resupauta
		widgets = {
			'fecha': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.nombre


class DetapautaForm(forms.ModelForm):
	class Meta:
		model = Detapauta
		widgets = {
			'fecha': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.paciente


class AnticiposForm(forms.ModelForm):
	class Meta:
		model = Anticipos
		widgets = {
			'fecha': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.rut


class Pacientes_auxForm(forms.ModelForm):
	class Meta:
		model = Pacientes_aux
		widgets = {
			'fe_ini': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		   	'fe_nac': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}

		fields = "__all__" 
		def __str__(self):
			return self.nombre


class Diario_auxForm(forms.ModelForm):
	class Meta:
		model = Diario_aux
		widgets = {
			'fecha': forms.TextInput(attrs={'input_formats': ["%d-%m-%Y H:i"]}),
		}
		fields = "__all__"

		def __str__(self):
			return self.paciente

class UploadFileForm(forms.Form):
	class Meta:
		model = UploadFile

		fields = "__all__"

		def __str__(self):
			return self.archivo

class RecetaForm(forms.ModelForm):
	class Meta:
		model = Receta

		fields = "__all__"

		def __str__(self):
			return self.rut


class MaefarmForm(forms.ModelForm):
	class Meta:
		model = Maefarm

		fields = "__all__"

		def __str__(self):
			return self.descrip
