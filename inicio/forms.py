from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import MySQLdb


class login2(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

class UserCreateForm(UserCreationForm):
	CUI = forms.IntegerField(required=True)
	first_name = forms.CharField(max_length=100, help_text='Nombre',required=True)
	last_name = forms.CharField(max_length=100, help_text='Apellido',required=True)
	puesto = forms.CharField(max_length=100, help_text='Puesto',required=True)
	class Meta:
		model = User
		fields = ("CUI","first_name","last_name","puesto","username", "password1", "password2")
