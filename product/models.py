from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField


User = get_user_model()


class Seller(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Business_Name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    contact_no=models.CharField(max_length=10)
    email = models.EmailField()
    is_verified = models.BooleanField(default=False)
    
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    
    token = models.UUIDField(default=uuid.uuid4,editable=False)
    slug = AutoSlugField(populate_from='title',unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0,help_text="in NRP",validators=[MinValueValidator(0),MaxValueValidator(4294967296)])
    discount = models.PositiveIntegerField(default=0,help_text="in %",validators=[MinValueValidator(0),MaxValueValidator(100)])
    seller = models.ForeignKey('Seller',on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/product',verbose_name='Image-product')