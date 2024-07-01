from django.urls import path
from .views import UserListView, UserDetailView, ProductDetailView,ProductListView

urlpatterns = [
    path("user/", UserListView.as_view(), name='users'),
    path("products/", ProductListView.as_view(), name='products'),
    path("user/<int:pk>/", UserDetailView.as_view(), name='userdetail'),
    path("product/<int:pk>/", ProductDetailView.as_view(), name='productdetail'),


]