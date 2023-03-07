from django.urls import path
from . import views


urlpatterns = [
    path("address/", views.AddressView.as_view()),
    path("address/<int:address_id>/", views.AddressDetailView.as_view()),
]
