from django.contrib import admin
from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwtviews

urlpatterns = [
    path("user/", views.RegisterUserView.as_view()),
    path("users/", views.ListUserView.as_view()),
    path("user/activate/<uuid:email_token>/", views.ActivateUser.as_view()),
    path("user/<uuid:user_id>/", views.UserDetailView.as_view()),
    path("user/<uuid:user_id>/restore/", views.RestoreUsersView.as_view()),
    path("access/<uuid:user_id>/", views.UserAccessSellerView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("login/access/", views.AccessLoginView.as_view()),
    # path("login/", jwtviews.TokenObtainPairView.as_view()),
    path("login/refresh/", jwtviews.TokenRefreshView.as_view()),
]
