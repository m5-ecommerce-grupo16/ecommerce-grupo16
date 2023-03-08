from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.CartView.as_view()),
    path("cart/<int:pk>/", views.CartDetailView.as_view()),
    path("cart/<int:pk>/cart_product/", views.AddProduct.as_view()),
]
