from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("seller/", views.RegisterSellerView.as_view()),
    path("sellers/", views.ListSellerView.as_view()),
    path(
        "seller/products/<uuid:seller_id>/", views.ListProductsForSellerView.as_view()
    ),
    path("seller/<uuid:seller_id>/", views.SellerDetailView.as_view()),
    path("seller/<uuid:seller_id>/restore/", views.RestoreSellersView.as_view()),
]
