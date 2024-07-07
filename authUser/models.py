from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
import uuid

class CustomManager(UserManager):
    def _create_user(self, phone_number,password,username=None , **extra_fields):
        """
        Create and save a user with the given username, phone_number, and password.
        """
        if username is None:
            username = phone_number
        user = User(phone_number=phone_number,username = username,**extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, phone_number,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    phone_number = models.CharField(max_length=10,unique=True)
    full_name = models.CharField(max_length=150,default='')
    gender = models.CharField(max_length=10,default='Male')
    birth_date = models.DateField(blank=True,null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    objects = CustomManager()



class Seller(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Business_Name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    contact_no=models.CharField(max_length=10)
    email = models.EmailField()
    is_verified = models.BooleanField(default=False)



class Buyer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField( max_length=254)
    shipping_address = models.CharField(max_length=254)
    gender = models.CharField(max_length=10)
    age=models.IntegerField()
