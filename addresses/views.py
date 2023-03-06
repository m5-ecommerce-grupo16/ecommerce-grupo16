from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Address
from .serializer import AddressSerializer


class AddressView(CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
