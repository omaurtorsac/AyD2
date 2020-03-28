# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    cliente = models.AutoField(primary_key=True)
    nit = models.CharField(db_column='NIT', max_length=10)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'


class Empleado(models.Model):
    cui = models.BigIntegerField(db_column='CUI', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.
    puesto = models.CharField(db_column='Puesto', max_length=45)  # Field name made lowercase.
    usuario = models.CharField(max_length=45)
    contrasenia = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Empleado'


class FacturaCompra(models.Model):
    no_factura = models.IntegerField(db_column='No_Factura', primary_key=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=45)  # Field name made lowercase.
    fecha = models.DateField()
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor', blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Factura_Compra'


class FacturaVenta(models.Model):
    no_factura = models.IntegerField(db_column='No_Factura', primary_key=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=45)  # Field name made lowercase.
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Factura_Venta'


class Producto(models.Model):
    producto = models.AutoField(db_column='Producto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'


class Proveedor(models.Model):
    proveedor = models.AutoField(primary_key=True)
    nit = models.CharField(db_column='NIT', max_length=10)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DetalleCompra(models.Model):
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.FloatField()
    factura = models.ForeignKey(FacturaCompra, models.DO_NOTHING, db_column='factura')
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto')

    class Meta:
        managed = False
        db_table = 'detalle_compra'
        unique_together = (('factura', 'producto'),)


class DetalleVenta(models.Model):
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.FloatField()
    factura = models.ForeignKey(FacturaVenta, models.DO_NOTHING, db_column='factura')
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto')

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('factura', 'producto'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
