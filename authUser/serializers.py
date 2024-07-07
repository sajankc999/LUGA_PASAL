from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerialier(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ['phone_number','full_name','gender','birth_date','password']
    def validate(self, attrs):
        phone_number = attrs['phone_number']
        if len(phone_number)!=10:
            return serializers.ValidationError('phone number must be 10 characters long')
        if len(attrs['password'])>65 or len(attrs['password'])<8:
            return serializers.ValidationError('password must be between 8 to 65 characters long')
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['phone_number','passoword']
        

class OtpSerializer(serializers.Serializer):
    otp=serializers.CharField(max_length=6)
    