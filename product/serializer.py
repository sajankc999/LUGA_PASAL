from .models import *
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    slug=serializers.CharField(required=False)
    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs ={'slug':{'read_only':True}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = Images
        fields='__all__'