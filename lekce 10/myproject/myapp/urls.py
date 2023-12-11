from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/registration/", views.registration, name="registration"),
]
