from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path("payments/token/", views.TokenView.as_view()),
    path("payments/pix/", views.PixView.as_view()),
]
