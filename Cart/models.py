from django.db import models
from product.models import *
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()

class Buyer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField( max_length=254)
    shipping_address = models.CharField(max_length=254)
    gender = models.CharField(max_length=10)


class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
