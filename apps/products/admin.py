from django.contrib import admin

# Register your models here.
from apps.products.models import ProductType, Product


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #No permite edicion de create y update
    list_display = ('name', 'quantity', 'price', 'description', 'mark', 'product_types')
    ordering = ('price','name','mark',
                'product_types') # En caso que sea una sola ordering('column',)
    #form de busqueda
    search_fields = ('name','mark', 'product_types__name') #Campo relacionado
    #date_hierarchy = 'create'    #campo de fechas
    list_filter = ('product_types__name',) # Campos relacionados

    """
    Para campos many to many
    def sale_products(self, obj):
        return ". ".join([c.name for c in obj.products.all().order_by("name")]) 
    
    sale_products.short_description = "Productos"
    """


admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
