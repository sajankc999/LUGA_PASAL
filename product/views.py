from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import generics,ModelViewSet
from .utils import verify_admin # verified admin returns true or false
from .permissions import ProductPermission
from rest_framework.response import Response
from rest_framework import status
import django_filters.rest_framework
from rest_framework.permissions import AllowAny,IsAuthenticated
from authUser.models import Seller,Buyer

class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[ProductPermission]
    lookup_field ='slug'
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    # def get_queryset(self):
    #     seller = self.request.user
    #     if Product.objects.filter(seller = seller ).exists():
    #         return Product.objects.filter(seller = seller )
    #     if verify_admin(seller):
    #         return Product.objects.all()
        
class ProductSellerView(ModelViewSet):
    # queryset=Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field ='slug'
    def get_queryset(self):
        seller = self.request.user
        if Product.objects.filter(seller = seller ).exists():
            return Product.objects.filter(seller = seller )
        if verify_admin(seller):
            return Product.objects.all()
        
    def create(self, request, *args, **kwargs):
        user = request.user
        if  not Seller.objects.filter(seller=user).exists():
            return Response('You need to verify as a seller to post goods')
        else:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(seller=user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
            

class PersonalizedFeedView(generics.ListAPIView):
    serializer_class =ProductSerializer
    permission_classes=[AllowAny]

    def get_queryset(self):
        user = self.request.user
        raise Exception(user)

        