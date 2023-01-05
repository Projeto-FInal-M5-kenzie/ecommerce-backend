from django.urls import path
from . import views

urlpatterns = [
    path("address/", views.AddressView.as_view()),
]