from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_employee = models.BooleanField(default=False)
    address = models.ForeignKey(
        "addresses.Address", on_delete=models.CASCADE, related_name="users"
    )
