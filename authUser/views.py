from django.shortcuts import render,redirect,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import *
from random import randint
from .utils import *
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.viewsets import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from datetime import datetime
from rest_framework.permissions import AllowAny
from pyotp import TOTP
from rest_framework.authtoken.models import Token  
from django.contrib.auth import authenticate

User=get_user_model()


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialier
    permission_classes=[AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
           
            data = serializer.validated_data
            # raise Exception(data)
            request.session['phone_number']=data['phone_number']
       
            # print("use daat is ",request.session['phone_number'])
         
            try:
                if User.objects.filter(phone_number=data.get('phone_number')).exists():
                    return Response({'message':'Phone number already exists'},status=status.HTTP_400_BAD_REQUEST)
                user =User.objects.create_user(**data,is_active=False)
                if user:
                    send_otp(request)
                    return Response({"message":"otp sent"},status=status.HTTP_201_CREATED)   
                
            except Exception as e:
                raise Exception(e)
            
class Otp_checkView(APIView):
    def post(self,request,Format=None):
        # raise Exception(request.POST)
        # otp =request.data.get('otp')
        serializer = OtpSerializer(data=request.data)
        # otp = request.POST.data['otp']
        # usename = request.session['username']
        if serializer.is_valid(raise_exception=True):
            otp = serializer.validated_data.get('otp')
            # int_otp=int(otp)
            # raise Exception(type(int(otp)))
            otp_secret_key = request.session['otp_secret_key']
            otp_valid_date = request.session['otp_valid_date']
            phone_number = request.session['phone_number']
            # raise Exception(otp_secret_key,otp_valid_date)
            if otp_secret_key and otp_valid_date is not None:
                valid_date = datetime.fromisoformat(otp_valid_date)
                if valid_date>datetime.now():
                    totp = pyotp.TOTP(otp_secret_key,interval=15*60)
                    # raise Exception(totp.verify(206953))
                    if totp.verify(otp):
                        user = User.objects.filter(phone_number=phone_number).first()
                        if user:
                            user.is_active=True
                            user.save()
                            del request.session['otp_secret_key']
                            del request.session['otp_valid_date']
                            del request.session['phone_number']
                            return Response ({"message":'verified succesfully','status':status.HTTP_201_CREATED})
                    else:
                        return Response ({"message":'otp didnt match','status':status.HTTP_400_BAD_REQUEST})
                else:
                    return Response ({"message":'otp expired','status':status.HTTP_400_BAD_REQUEST})
                        
    

# def verify_otp(request):
#     context={}
#     if request.method=='POST':
        
#         otp = request.POST['otp']
#         # usename = request.session['username']
#         otp_secret_key = request.session['otp_secret_key']
#         otp_valid_date = request.session['otp_valid_date']
#         phone_number = request.session['phone_number']
#         if otp_secret_key and otp_valid_date is not None:
#             valid_date = datetime.fromisoformat(otp_valid_date)
#             if valid_date>datetime.now():
#                 totp = pyotp.TOTP(otp_secret_key,interval=15*60)
#                 if totp.verify(otp):
#                     user = User.objects.filter(phone_number=phone_number).first()
#                     if user:
#                         user.is_active=True
#                         user.save()
#                         del request.session['otp_secret_key']
#                         del request.session['otp_valid_date']
#                         del request.session['phone_number']
#                         context={"message":'verified succesfully','status':status.HTTP_201_CREATED}
#                 else:
#                     context={"message":'otp didnt match','status':status.HTTP_400_BAD_REQUEST}
#             else:
#                 context={"message":'otp expired','status':status.HTTP_400_BAD_REQUEST}
                       
            
    # return render(request,'otp.html',context=context)            

    
        
     







class loginViewset(APIView):
    def post(self,request):
        try:
            username=request.data.username
            password=request.data.password
            serializer = LoginSerializer(data = request.data)
            if not serializer.is_valid():
                return Response({
                    "message":serializer.errors,
                    })
            serializer.save()
            user = authenticate(username=username,password = password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                return Response({
                    "username":user.get_username(),
                    "token":token.key,                    
                })
        except Exception as e:
            return Response({"error":e,})