from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth import get_user_model
User = get_user_model()


admin.site.register(User)
admin.site.register(Buyer)
admin.site.register(Seller)