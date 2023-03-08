from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("order/", views.OrderView.as_view()),
    path("order/<int:pk>/", views.OrderDetailView.as_view()),
]
