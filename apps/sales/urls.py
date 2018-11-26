from django.urls import path
from apps.sales.views import index


urlpatterns = [
    path('', index, name='index'),
]