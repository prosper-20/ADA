from django.shortcuts import render
from django.urls import path
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductHomePage(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailPage(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"

    
