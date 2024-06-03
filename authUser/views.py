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
from rest_framework.authtoken.models import Token
from datetime import datetime
from pyotp import TOTP
User=get_user_model()


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialier


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
          
            data = serializer.validated_data
            request.session.modified = True
            request.session['phone_number']=serializer.validated_data.get('phone_number')
       
            print("use daat is ",request.session['phone_number'])
         
            try:
                send_otp(request)
            except Exception as e:
                raise Exception(e)
            finally:
                if User.objects.filter(phone_number=data.get('phone_number')).exists():
                    return Response({'message':'Phone number already exists'},status=status.HTTP_400_BAD_REQUEST)
                user =User.objects.create_user(**data)
                if user:
                    return Response({"message":"User created"},status=status.HTTP_201_CREATED)                  
            return Response('otp send')

       
        
     



def verify_otp(request):
    context={}
    if request.method=='POST':
        
        otp = request.POST['otp']
        # usename = request.session['username']
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_date = request.session['otp_valid_date']
        phone_number = request.session['phone_number']
        if otp_secret_key and otp_valid_date is not None:
            valid_date = datetime.fromisoformat(otp_valid_date)
            if valid_date>datetime.now():
                totp = pyotp.TOTP(otp_secret_key,interval=15*60)
                if totp.verify(otp):
                    user = User.objects.filter(phone_number=phone_number).first()
                    if user:
                        user.is_verified=True
                        user.save()
                        del request.session['otp_secret_key']
                        del request.session['otp_valid_date']
                        del request.session['phone_number']
                        context={"message":'verified succesfully','status':status.HTTP_201_CREATED}
                else:
                    context={"message":'otp didnt match','status':status.HTTP_400_BAD_REQUEST}
            else:
                context={"message":'otp expired','status':status.HTTP_400_BAD_REQUEST}
                       
            
    return render(request,'otp.html',context=context)


