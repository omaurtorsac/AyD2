# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from .models import *
from django.db.models import Q

def productoexiste(nombre, marca):
	p = Producto.objects.filter(nombre = nombre).filter(marca = marca)
	return p

def empleadoexiste(cui,usuario):
	e = Empleado.objects.filter(Q(cui=cui)|Q(usuario=usuario))
	return e

def nitexiste(nit):
	n = Cliente.objects.filter(nit = nit)
	return n

def nitexiste2(nit):
	n = Proveedor.objects.filter(nit = nit)
	return n

def reporteno1():
	r1 = Producto.objects.values_list('nombre','marca','cantidad')
	return r1