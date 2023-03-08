from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from .models import Product
from .serializer import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrSuperuser
from .serach import ProductGetView


class ProductView(CreateAPIView, ProductGetView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrSuperuser]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        return serializer.save(id=self.kwargs["pk"])

    def perform_destroy(self, instance):
        return instance.delete()
