from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
import MySQLdb

class productos(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ("nombre", "marca","cantidad")

class clientes(forms.ModelForm):
	nit = forms.IntegerField(required = True, help_text='Ingrese solo digitos')
	class Meta:
		model = Cliente
		fields = ("nit", "nombre","apellido")

class proveedores(forms.ModelForm):
	nit = forms.IntegerField(required = True, help_text='Ingrese solo digitos')
	class Meta:
		model = Proveedor
		fields = ("nit", "nombre","apellido")

class login2(AuthenticationForm):
	#usuario = forms.CharField(widget=forms.TextInput,required=True)
    #password = forms.CharField(widget=forms.PasswordInput(),required=True)
	class Meta:
		model = User
		fields = ("username","password")
    

class UserCreateForm(UserCreationForm):
	CUI = forms.IntegerField(required=True)
	first_name = forms.CharField(max_length=100, help_text='Nombre',required=True)
	last_name = forms.CharField(max_length=100, help_text='Apellido',required=True)
	puesto = forms.CharField(max_length=100, help_text='Puesto',required=True)
	class Meta:
		model = User
		fields = ("CUI","first_name","last_name","puesto","username", "password1", "password2")
