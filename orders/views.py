from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Order, Order_Product
from .serializer import OrderSerializer, Order_ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OrderView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AddOrder(ListCreateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order_Product.objects.all()
    serializer_class = Order_ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(order_id=self.kwargs["pk"])
