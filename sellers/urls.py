from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("sellers/", views.RegisterSellerView.as_view()),
    path("sellers/<int:seller_id>/", views.SellerDetailView.as_view()),
]
