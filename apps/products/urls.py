from django.urls import path
from apps.products.views import index, product_view, product_list, product_edit, product_delete, ProductList, \
    ProductCreate, ProductUpdate, ProductDelete

app_name = 'producto'
urlpatterns = [
    path('', index, name='index'),
    #path('nuevo/', product_view, name='product_new'),
    #path('listar/', product_list, name='product_list'),
    #path('editar/<int:id_product>/', product_edit, name='product_edit'),
    #path('eliminar/<int:id_product>/', product_delete, name='product_delete'),
    path('nuevo/', ProductCreate.as_view(), name='product_new'),
    path('listar/', ProductList.as_view(), name='product_list'),
    path('editar/<int:pk>/', ProductUpdate.as_view(), name='product_edit'),
    path('eliminar/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
]