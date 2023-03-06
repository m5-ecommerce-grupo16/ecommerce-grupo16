from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("order/", views.OrderView.as_view()),
    path("order/<int:order_id>/", views.OrderDetailView.as_view()),
]
