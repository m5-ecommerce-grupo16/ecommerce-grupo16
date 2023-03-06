from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Cart
from .serializer import CartSerializer


class CartView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
