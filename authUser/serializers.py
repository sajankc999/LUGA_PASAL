from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerialier(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ['phone_number','Full_name','Gender','Birth_date','password']


