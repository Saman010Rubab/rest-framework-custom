from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Product
from .serializers import UserSerializer, ProductSerializer
from django.contrib.auth.models import User


class UserListView(generics.ListCreateAPIView):
    queryset =User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductListView(generics.ListCreateAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]