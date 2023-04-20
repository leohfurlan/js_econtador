from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register_usuario", views.register, name="register_usuario")
]