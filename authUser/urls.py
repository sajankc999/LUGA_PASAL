
from django.urls import path
from .views import *
urlpatterns = [
    path('user/create/',UserView.as_view()),
    path('otp/',verify_otp)
 
    
]