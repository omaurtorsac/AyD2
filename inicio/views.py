from django.shortcuts import render, render_to_response
from .forms import *
from .consultas import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login as do_login
from django.contrib.auth.decorators import login_required

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


def adminp(request):
	mensaje="Bienvenido a la pagina del administrador!"
	return render(request,'inicio/adminp.html',{'mensaje':mensaje});

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('../');

def proveedor(request):
	#form = login2(request.POST)
	form = proveedores()
	mensaje = "Registre nuevo proveedor"
	variables={
		"form":form,
		"mensaje":mensaje,
	}
	if request.method == "POST":
		form = proveedores(data=request.POST)
		if form.is_valid():
			datos = form.cleaned_data
			nombre = datos.get('nombre')
			nit = datos.get('nit')
			apellido = datos.get('apellido')
			n = nitexiste(nit)
			if not n:
				form.save()
				form = proveedores()
				mensaje = "Proveedor registrado"
				variables={
					"form":form,
					"mensaje":mensaje,
				}
			else:
				mensaje = "Nit ya existente en la base de datos"
				variables = {
					"form":form,
					"mensaje":mensaje,
				}
		else:
			mensaje = "Error al grabar"
			variables = {
				"form": form,
				"mensaje":mensaje,
			}
	else:
		mensaje="Error en datos ingresados"
	return render(request, "inicio/proveedores.html", variables)


def reporte1(request):
	mensaje1 = "Reporte de Productos"
	camp = ['Nombre del producto','Marca','Cantidad en bodega']
	r1 = reporteno1()
	variables = {
		"mensaje1":mensaje1,
		"campos":camp,
		"r1":r1,
	}
	print(r1)
	return render(request, "inicio/reporte1.html",variables)

def cliente(request):
	#form = login2(request.POST)
	form = clientes()
	mensaje = "Registre nuevo cliente"
	variables={
		"form":form,
		"mensaje":mensaje,
	}
	if request.method == "POST":
		form = clientes(data=request.POST)
		if form.is_valid():
			datos = form.cleaned_data
			nombre = datos.get('nombre')
			nit = datos.get('nit')
			apellido = datos.get('apellido')
			n = nitexiste(nit)
			if not n:
				form.save()
				form = clientes()
				mensaje = "Cliente registrado"
				variables={
					"form":form,
					"mensaje":mensaje,
				}
			else:
				mensaje = "Nit ya existente en la base de datos"
				variables = {
					"form":form,
					"mensaje":mensaje,
				}
		else:
			mensaje = "Error al grabar"
			variables = {
				"form": form,
				"mensaje":mensaje,
			}
	else:
		mensaje="Error en datos ingresados"
	return render(request, "inicio/clientes.html", variables)

def producto(request):
	#form = login2(request.POST)
	form = productos()
	mensaje = "Registre nuevo producto"
	variables={
		"form":form,
		"mensaje":mensaje,
	}
	if request.method == "POST":
		form = productos(data=request.POST)
		if form.is_valid():
			datos = form.cleaned_data
			nombre = datos.get('nombre')
			marca = datos.get('marca')
			p = productoexiste(nombre,marca)
			if  not p:
				form.save()
				form = productos()
				mensaje = "Producto grabado"
				variables={
					"form":form,
					"mensaje":mensaje,
				}
			else:
				form = productos()
				mensaje = "Producto con ese tipo de marca ya existente"
				variables = {
					"form":form,
					"mensaje":mensaje,
				}
		else:
			mensaje = "Error al grabara"
			variables = {
				"form": form,
				"mensaje":mensaje,
			}
	else:
		mensaje="Error en datos ingresados"
	return render(request, "inicio/productos.html", variables)


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
			cu = empleadoexiste(CUI)
			if not cu:
				form.save()
				form = UserCreateForm()
				mensaje = "Empelado registrado"
			#db = MySQLdb.connect(host=rds_host, user=user_name, password=password, db=db_name, connect_timeout=5)
			#c = db.cursor()
			#print("connected to db server")
			#consulta = "INSERT INTO Empleado VALUES("+str(CUI)+",'"+nombre+"','"+apellido+"','"+puesto+"','"+username+"','"+contra+"');"
			#consulta2 = "SELECT CUI, usuario from Empleado WHERE CUI = "+str(CUI)+" OR usuario = '"+username+"';"
			#print(consulta2)
			#c.execute(consulta2)
			#a = c.rowcount
			else:
				form = UserCreateForm()
				mensaje = "CUI o Username ya creado en base de datos"
				variables = {
					"form":form,
					"mensaje":mensaje,
				}
		else:
			mensaje = "Error al grabar"
			variables = {
				"form": form,
				"mensaje":mensaje,
			}
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


def adminp(request):
    mensaje="Bienvenido a la pagina del administrador!"
    return render(request,'inicio/adminp.html',{'mensaje':mensaje});

def login(request):
	#form = login2(request.POST)
	form = login2()
	variables={
		"form":form,
	}
	
	if request.method == "POST":
		form = login2(data=request.POST)
		if form.is_valid():
			datos = form.cleaned_data
			user = datos.get("username")
			psw = datos.get("password")
			usuario = auth.authenticate(username = user, password = psw)
			if usuario is not None:
				do_login(request,usuario)
				auth.login(request, usuario)
				return HttpResponseRedirect('../adminp');
			else:
				form = login2()
				variables = {
					"form": form,
				}
				return render(request, "inicio/login.html", {"form": form})   #if user == row[0]:
					#	print("encontro")
					#else
					#return render_to_response('inicio/login.html',{"form":form})
		else:
			variables = {
				"form": form,
			}
	return render(request, "inicio/login.html", variables)
