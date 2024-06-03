from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password


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
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    phone_number = models.CharField(max_length=10,unique=True)
    Full_name = models.CharField(max_length=150,default='')
    Gender = models.CharField(max_length=10,default='Male')
    Birth_date = models.DateField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    objects = CustomManager()
