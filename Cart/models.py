from django.db import models
from product.models import *
from django.contrib.auth import get_user_model
import uuid
from authUser.models import Buyer
User = get_user_model()
class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
