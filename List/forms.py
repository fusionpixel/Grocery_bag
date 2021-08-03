from django import forms
from django.db.models.fields import DateField
from django.forms import ModelForm
from .models import AddItem

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddItemForm(ModelForm):
    class Meta:
        model = AddItem
        fields = ["name", "quantity", "status", "date"]
        labels = {
            "name": "Item Name",
            "quantity": "Item Quantity",
            "status": "Item Status",
            "date": "Date",
        }
        STATUS_CHOICES = [
            ("PENDING", "PENDING"),
            ("BOUGHT", "BOUGHT"),
            ("NOT AVAILABLE", "NOT AVAILABLE"),
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Item name"}
            ),
            "quantity": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Item quantity"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(
                attrs={"type": "date", "class": "form-control", "placeholder": "Date"}
            ),
        }


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "username",
                "class": "form-control",
                "id": "username",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "type": "text",
                "name": "email",
                "class": "form-control",
                "id": "email",
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "name": "password1",
                "class": "form-control",
                "id": "password1",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "name": "password2",
                "class": "form-control",
                "id": "password2",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")

        if (
            email
            and User.objects.filter(email=email).exclude(username=username).exists()
        ):
            raise forms.ValidationError("This email has already been registered.")

        return email
