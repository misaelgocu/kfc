from django.db import models

# Create your models here.
class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(unique=True, max_length=150)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'empresas'


class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='id_empresa')
    nombre_marca = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'marcas'


class Sucursales(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='id_marca')
    cc_suc = models.PositiveIntegerField(unique=True)
    compania = models.PositiveIntegerField()
    nombre_sucursal = models.CharField(max_length=100)
    fecha_inicio_suc = models.IntegerField(blank=True, null=True)
    fecha_fin_suc = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'sucursales'


class Ventas(models.Model):
    id_dft = models.PositiveBigIntegerField(primary_key=True)
    id_sucursal = models.ForeignKey(Sucursales, models.DO_NOTHING, db_column='id_sucursal')
    fecha_dft = models.IntegerField()
    fecha = models.DateField()
    periodo = models.CharField(max_length=50, blank=True, null=True)
    semana = models.CharField(max_length=50, blank=True, null=True)
    vtas_netas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    iva_comedor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_iva_por_pagar = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    iva_llevar = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vtas_comedor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vtas_llevar = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vtas_entrega = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    iva_entrega = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    iva_ventana = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    vtas_ventana = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    reembolso_cliente = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
