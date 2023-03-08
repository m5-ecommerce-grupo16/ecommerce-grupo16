from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    DestroyAPIView,
)
from .models import Cart, Cart_Product
from .serializer import CartSerializer, CartProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CartView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)


class CartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class AddProduct(ListCreateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Cart_Product.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        return serializer.save(cart_id=self.kwargs["pk"])
