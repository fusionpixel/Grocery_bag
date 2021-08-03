from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AddItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=25)

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("BOUGHT", "BOUGHT"),
        ("NOT AVAILABLE", "NOT AVAILABLE"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    date = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
