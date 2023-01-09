from django.urls import path
from . import views


urlpatterns = [
    path(
        "address/users/",
        views.AddressViewUser.as_view(),
    ),
    path(
        "address/sellers/<uuid:seller_id>/",
        views.AddressViewSeller.as_view(),
    ),
]
