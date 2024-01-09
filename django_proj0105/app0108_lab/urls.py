from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
]
