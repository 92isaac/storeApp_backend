from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from .models import Category, Product
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer