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

    serializer_class = CartProductSerializer
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        cart_product_exist = Cart_Product.objects.filter(
            cart_id=self.request.user.cart_id, product_id=self.request.data['product'])
        if cart_product_exist.count() == 0:
            Cart_Product.objects.create(
                cart_id=self.request.user.cart_id, product_id=self.request.data['product'], ammount=self.request.data['ammount'])
        else:
            cart_product_exist.update(ammount=self.request.data['ammount'])
