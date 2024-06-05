from django.db import models
from Cart.models import *
import uuid



class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)


class OrderItem(models.Model):
    key = models.UUIDField(default=uuid.uuid4)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    