from django.urls import path
from . import views


urlpatterns = [
    path(
        "product/",
        views.ProductView.as_view(),
    ),
    path(
        "product/category/<uuid:category_id>/",
        views.ProductCategoryView.as_view(),
    ),
    path(
        "product/<uuid:product_id>/order/",
        views.OrderProductView.as_view(),
    ),
]
