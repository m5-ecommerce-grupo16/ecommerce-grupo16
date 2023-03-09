from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
)
from .models import Cart, Cart_Product
from .serializer import CartSerializer, CartProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class CartView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    serializer_class = CartSerializer

    def get_queryset(self):
        cart_queryset = Cart.objects.filter(id=self.request.user.cart_id)
        return cart_queryset


class CartAddView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    queryset = Cart_Product.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        serializer.save(cart=self.request.user.cart)
