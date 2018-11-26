from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
from apps.products.models import Product

class Sale(models.Model):
    date = models.DateField(default=now)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"


    def __str__(self):
        return self.name

class Membership(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    date_sale = models.DateField()
    price = models.IntegerField()
    quantity = models.IntegerField()
