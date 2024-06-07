from django.db import models
from Cart.models import *
import uuid



class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    buyer = models.ForeignKey("Cart.Buyer",on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4,editable=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    