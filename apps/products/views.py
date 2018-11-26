from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.products.form import ProductForm
from apps.products.models import Product


def index(request):
    return render(request, 'products/index.html')

def product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('producto:index')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form':form})

def product_list(request):
    product = Product.objects.all().order_by('-id')
    context = {'products':product}
    return render(request, 'products/product_list.html', context)

def product_edit(request, id_product):
    product = Product.objects.get(pk=id_product)
    if request.method == 'GET':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('producto:product_list')

    return render(request, 'products/product_form.html', {'form':form})

def product_delete(request, id_product):
    product = Product.objects.get(pk=id_product)
    if request.method == 'POST':
        product.delete()
        return redirect('producto:product_list')
    return render(request, 'products/product_delete.html', {'products': product})

class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('producto:product_list')

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('producto:product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('producto:product_list')