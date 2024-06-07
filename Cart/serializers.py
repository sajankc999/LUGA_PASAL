from rest_framework import serializers
from .models import *

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields="__all__"
        lookup_field ='uuid'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields= '__all__'