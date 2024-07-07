from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.viewsets import generics,ModelViewSet
from product.utils import verify_admin
class BuyerView(ModelViewSet):
    serializer_class = BuyerSerializer
    lookup_field='uuid'
    def get_queryset(self):
        if Buyer.objects.filter(user = self.request.user):
            return Buyer.objects.filter(user=self.request.user)
        return Response({"message":"dosent exists"})
    

class CartItemView(ModelViewSet):
    serializer_class=CartItemSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user:
            return CartItem.objects.filter(cart__buyer=user)
        if verify_admin(user):
            return CartItem.objects.all()
        
    