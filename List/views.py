from django.http.request import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db import IntegrityError

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import AddItem
from .forms import AddItemForm, CreateUserForm
from datetime import datetime, date

# from .filters import ItemFilter

# ADMIN CREDENTIALS = [Vasanth, 12345678]
# USER LOGIN = [fury, azxcvbnm]


# Create your views here.


def home(request):
    return render(request, "home.html")


def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect("loginpage")
        else:
            messages.warning(request, "There was an error creating your account")

    context = {"form": form}
    return render(request, "signup.html", context)

    # if request.method == "GET":
    #     return render(request, "signup.html", {"form": UserCreationForm()})
    # else:
    #     if request.POST["password1"] == request.POST["password2"]:
    #         try:
    #             user = User.objects.create_user(
    #                 request.POST["username"], password=request.POST["password1"]
    #             )
    #             user.save()
    #             login(request, user)
    #             return redirect(index)
    #         except IntegrityError:
    #             return render(
    #                 request,
    #                 "signup.html",
    #                 {
    #                     "form": UserCreationForm(),
    #                     "error": "This Username has already been taken. Please choose a new username",
    #                 },
    #             )
    #     else:
    #         return render(
    #             request,
    #             "signup.html",
    #             {"form": UserCreationForm(), "error": "Passwords did not match"},
    #         )


def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invlaid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


@login_required
def logout_view(request):
    # if request.method == "POST":
    logout(request)
    return redirect("loginpage")


@login_required
def index(request):
    items = AddItem.objects.filter(user=request.user)
    dateToFilter = request.POST.get("dateToFilter")
    if dateToFilter is not None:
        if dateToFilter == "":
            items = AddItem.objects.filter(user=request.user)
        else:
            year, month, xdate = map(int, dateToFilter.split("-"))
            items = AddItem.objects.filter(
                user=request.user, date__year=year, date__month=month, date__day=xdate
            )

    context = {"items": items}
    return render(request, "index.html", context)


@login_required
def add_item(request):
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            newItem = form.save(commit=False)
            newItem.user = request.user
            newItem.save()
            return redirect("index")
    else:
        form = AddItemForm()
    return render(request, "add.html", {"form": form})


@login_required
def update_item(request, item_id):
    item = AddItem.objects.get(pk=item_id, user=request.user)
    form = AddItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "update.html", {"item": item, "form": form})


@login_required
def delete(request, item_id):
    item = AddItem.objects.get(pk=item_id, user=request.user)
    # if request.method == "POST":
    item.delete()
    return redirect("index")
