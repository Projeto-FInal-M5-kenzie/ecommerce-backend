from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.CategoryView.as_view()),
    path("category/<uuid:category_id>/", views.CategoryDetailView.as_view()),
    path("category/<uuid:category_id>/restore/", views.RestoreCategoryView.as_view()),
]
