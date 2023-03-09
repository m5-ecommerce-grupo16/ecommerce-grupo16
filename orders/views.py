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
from django.shortcuts import get_object_or_404


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

    def create(self, request, *args, **kwargs):
        # Criando a ordem
        order = Order.objects.create(user=self.request.user)

        # Adicionando produtos na ordem
        cart = Cart.objects.get(user=self.request.user)
        cart_products = Cart_Product.objects.filter(cart=cart)

        for cart_product in cart_products:
            product = cart_product.product
            quantity = cart_product.ammount
            if product.quantity >= quantity:
                Order_Product.objects.create(order=order, product=product)
                product.quantity -= quantity
                product.save()
            else:
                # Caso não tenha quantidade suficiente, retornamos uma mensagem de erro
                return Response(
                    {
                        "error": "Não há quantidade suficiente do produto "
                        + product.name
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Atualizando o total da ordem
        order.save()

        # Deletando o carrinho do usuário
        cart_products.delete()

        serializer = self.serializer_class(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
