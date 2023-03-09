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
        print(self.request.user.cart)


class CartAddView(CreateAPIView):
    queryset = Cart_Product.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    serializer_class = CartProductSerializer
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        cart_queryset = Cart.objects.filter(user_id=self.request.user.id)

        if cart_queryset.count() == 0:
            Cart.objects.create(user_id=self.request.user.id)
            cart_queryset = Cart.objects.filter(user_id=self.request.user.id)

        cart_id = cart_queryset[0].id

        cart_product_exist = Cart_Product.objects.filter(
            cart_id=cart_id, product_id=self.request.data["product"])

        if cart_product_exist.count() == 0:
            serializer.save(cart_id=cart_id)
        else:
            print("product exist")
