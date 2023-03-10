from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Order_Product
from carts.models import Cart, Cart_Product
from .serializer import OrderSerializer, Order_ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from orders.models import Status


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AddOrder(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Order_ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status=Status.SUCCESS)
