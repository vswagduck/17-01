from django.shortcuts import render
from rest_framework import status, permissions, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CartSerializer, CartItemSerializer, CategorySerializer, ProductSerializer
from .models import Cart, CartItem, Category, Product
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_csv import renderers


# Create your views here.

class CategoryGenericCreateList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def list(self, request, *args, **kwargs):


class CategoryGenericRetriveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartGeneririCreateList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartGenericRetriveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemGeneririCreateList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemGenericRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class ProductGeneririCreateList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductGenericRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductExport(APIView):
    renderer_classes = (renderers.CSVRenderer,)

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class ProductsCreate_list(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsDDU(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
