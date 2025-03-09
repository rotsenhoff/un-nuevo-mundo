
from django.db import models

class Cliente(models.Model):
    nombre= models.CharField(max:length=64)
    apellidos = models.CharField(max:length=64)
    rfc = models.CharField(max:length=15,unique=True)
    fecha_nacimiento = models.DateField() 
    activo = models.BoolField(default=True)

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    importe = models.DecimalField(max_digits=8, decimal_digits=2)
    pagada = models.BoolField(default=False)

from contabilidad.models import Cliente, Factura
import datetime

fecha_nacimiento = datetime.date(1980, 12, 5)
pedro = Cliente(
    nombre="Pedro",
    apellidos="Aguilar Ramírez",
    rfc="AGRM-801205-111",
    fecha_nacimiento=fecha_nacimiento, activo=True,
)
pedro.save()

