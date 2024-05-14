from django.urls import path
from .views import produits, stocks, ventes

urlpatterns = [
    path('produits/', produits.list_products, name="list_products")
]