from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginpage, name="loginpage"),
    path("logout/", views.logout_view, name="logout"),
    path("add/", views.add_item, name="add_item"),
    path("update/<item_id>", views.update_item, name="update_item"),
    path("delete/<item_id>", views.delete, name="delete"),
]
