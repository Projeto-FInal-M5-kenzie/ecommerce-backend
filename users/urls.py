from django.contrib import admin
from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwtviews

urlpatterns = [
    path("users/", views.RegisterUserView.as_view()),
    path("users/<uuid:user_id>/", views.UserDetailView.as_view()),
    path("access/<uuid:user_id>/", views.UserAccessSellerView.as_view()),
    path("login/", jwtviews.TokenObtainPairView.as_view()),
]
