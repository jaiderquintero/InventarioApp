# Generated by Django 2.1.3 on 2018-11-23 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Descuento')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sub Total')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sale', models.DateTimeField(auto_now=True, verbose_name='fecha')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Producto')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sale', verbose_name='Venta')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ManyToManyField(through='sales.SaleProduct', to='products.Product', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='sale',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
