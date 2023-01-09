from django.urls import path
from . import views


urlpatterns = [
    path(
        "product/",
        views.ProductView.as_view(),
    ),
    path(
        "product/<uuid:product_id>/",
        views.ProductDetailView.as_view(),
    ),
    path(
        "product/order_product/",
        views.OrderProductView.as_view(),
    ),
    path(
        "product/order_product/",
        views.OrderProductView.as_view(),
    ),
    path(
        "product/order_product/<uuid:order_product_id>/",
        views.OrderProductDetailView.as_view(),
    ),
]
