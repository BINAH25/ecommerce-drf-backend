from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seraliazers import *
from .models import *
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response('hello')

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk=None):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product,many=False)     
    return Response(serializer.data)