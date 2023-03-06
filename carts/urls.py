from django.urls import path
from . import views


urlpatterns = [
    path("cart/", views.CartView.as_view()),
    path("cart/<int:cart_id>/", views.CartDetailView.as_view()),
]
