from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .serializer import ProductSerializer
from .models import Product


class ProductGetView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = ProductSerializer

    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get("category", None)
        product_id = self.request.query_params.get("id", None)
        name = self.request.query_params.get("name", None)
        description = self.request.query_params.get("description", None)
        user_id = self.request.query_params.get("user_id", None)

        if category is not None:
            queryset = queryset.filter(category__icontains=category)
        if product_id is not None:
            queryset = queryset.filter(id=product_id)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if description is not None:
            queryset = queryset.filter(description__icontains=description)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
