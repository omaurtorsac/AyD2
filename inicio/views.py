from django.shortcuts import render, render_to_response
from .forms import login2
from .forms import UserCreateForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login as do_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

import os
import subprocess
import MySQLdb
# Create your views here.

rds_host = 'django.c8c05aosp5rj.us-east-1.rds.amazonaws.com'
db_name = 'django'
user_name = 'admin'
password = 'admin.1234'
port = 3306

def index(request):
	return render_to_response('inicio/index.html');

@login_required
def adminp(request):
	mensaje="Bienvenido a la pagina del administrador!"
	return render(request,'inicio/adminp.html',{'mensaje':mensaje});

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('../');

@login_required
def registro(request):
	# Creamos el formulario de autenticación vacío

	form = UserCreateForm()
	mensaje = "Nuevo usuario a la plataforma"
	variables={
		"form":form,
		"mensaje":mensaje,
	}
	if request.method == "POST":
		# Añadimos los datos recibidos al formulario
		form = UserCreateForm(data=request.POST)
        # Si el formulario es válido...
		if form.is_valid():
			datos = form.cleaned_data
			CUI = datos.get('CUI')
			nombre = datos.get('first_name')
			apellido = datos.get('last_name')
			username = datos.get('username')
			puesto = datos.get('puesto')
			contra = datos.get('password1')
			
			
			db = MySQLdb.connect(host=rds_host, user=user_name, password=password, db=db_name, connect_timeout=5)
			c = db.cursor()
			print("connected to db server")
			consulta = "INSERT INTO Empleado VALUES("+str(CUI)+",'"+nombre+"','"+apellido+"','"+puesto+"','"+username+"','"+contra+"');"
			print(consulta)
			user = form.save()
			if user is not None:
				c.execute(consulta)
				db.commit()
				c.close()
				mensaje = "Usuario creado correctamente"
				form = UserCreateForm()
				variables={
					"form":form,
					"mensaje":mensaje,
				}
				return render(request, "inicio/registro.html", variables)
			else:
				mensaje = "Usuario ya existente"
				variables={
					"form":form,
					"mensaje":mensaje,
				}
				return render(request, "inicio/registro.html", variables)
		else:
			print("llego aquí")
            # Creamos la nueva cuenta de usuario
            #user = form.save()

            # Si el usuario se crea correctamente 
            #if user is not None:
                # Hacemos el login manualmente
            #    do_login(request, user)
                # Y le redireccionamos a la portada
            #    return redirect('/')

    # Si llegamos al final renderizamos el formulario
	return render(request, "inicio/registro.html", variables)

@login_required
def adminp(request):
    mensaje="Bienvenido a la pagina del administrador!"
    return render(request,'inicio/adminp.html',{'mensaje':mensaje});

def login(request):
	form = login2(request.POST)
	mensaje = "Hola"
	variables={
		"form":form,
		"mensaje":mensaje,
	}
	if form.is_valid():
		datos = form.cleaned_data
		user = datos.get("usuario")
		psw = datos.get("password")
		usuario = auth.authenticate(username = user, password = psw)
		if usuario is not None:
			do_login(request,usuario)
			auth.login(request, usuario)
			return HttpResponseRedirect('../adminp');
		else:
			mensaje = "Usuario o Password incorrecto"
			variables = {
				"form": form,
				"mensaje": mensaje,
			}
			return render(request, "inicio/login.html", {"form": form, "mensaje": mensaje})   #if user == row[0]:
				#	print("encontro")
				#else
				#return render_to_response('inicio/login.html',{"form":form})
	return render(request, "inicio/login.html", variables)
