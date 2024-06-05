from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prodcut = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    Rating = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(5)])
    comment = models.TextField()

