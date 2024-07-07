from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField
from .slug import unique_slugify
from authUser.models import Seller
User = get_user_model()


    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
class Targeted_age(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    token = models.UUIDField(default=uuid.uuid4,editable=False)
    slug = models.SlugField(max_length=50,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0,help_text="in NRP",validators=[MinValueValidator(0),MaxValueValidator(4294967296)])
    discount = models.PositiveIntegerField(default=0,help_text="in %",validators=[MinValueValidator(0),MaxValueValidator(100)])
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    targeted_age = models.ForeignKey(Targeted_age,on_delete=models.CASCADE)

    def save(self,**kwargs) -> None:
        slug = '%s' % (self.title)
        unique_slugify(self, slug)
        super(Product, self).save()


class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/product',verbose_name='Image-product')