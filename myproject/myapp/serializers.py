from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'username', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value


class ProductSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')
    class Meta:
        model= Product
        fields = ['id', 'product_name', 'description', 'added_by']

    def validate_product_name(self, value):
        if Product.objects.filter(product_name=value).exists():
            raise serializers.ValidationError("This product is already exists.")
        return value

