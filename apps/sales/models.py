from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
from apps.products.models import Product

class Sale(models.Model):
    date = models.DateField(default=now, verbose_name="Fecha")
    discount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Descuento")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sub Total")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    user= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    product = models.ManyToManyField(Product, through='SaleProduct', verbose_name="Producto")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"


class SaleProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Venta")
    date_sale = models.DateTimeField(auto_now=True, verbose_name="fecha")
    price = models.IntegerField(verbose_name="Precio")
    quantity = models.IntegerField(verbose_name="Cantidad")


