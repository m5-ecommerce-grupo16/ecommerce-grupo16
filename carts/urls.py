from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.CartView.as_view()),
    path("cart/add/", views.CartAddView.as_view()),
]
