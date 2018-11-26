from django import forms
from apps.products.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'name',
            'quantity',
            'price',
            'description',
            'mark',
            'product_types',
        ]

        labels = {
            'name':'Nombre',
            'quantity':'Cantidad',
            'price':'Precio',
            'description':'Descripcion',
            'mark':'Marca',
            'product_types':'Tipo Producto',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'mark':forms.TextInput(attrs={'class':'form-control'}),
            'product_types':forms.Select(attrs={'class':'form-control'}),  #para realacion 1 a muchos y forms.CheckboxSelectMultiple muchos a muchos
        }