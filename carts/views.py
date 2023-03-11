from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cart, Cart_Product
from products.models import Product
from .serializer import CartSerializer, CartProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError


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
        product_id = serializer.validated_data['product'].id
        ammount = serializer.validated_data['ammount']

        existing_product = Product.objects.get(id=product_id)

        if existing_product and existing_product.quantity >= ammount:
            serializer.save(cart=self.request.user.cart,
                            product=existing_product)
        else:
            raise ValidationError({"error": "Not enough products in stock"})


class CartRemoveDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    queryset = Cart_Product.objects.all()
    serializer_class = CartProductSerializer

    def perform_destroy(self, instance):
        return instance.delete()
