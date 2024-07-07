
from django.db.models.signals import post_save, pre_delete
from .models import Buyer,Cart
from django.dispatch import receiver


@receiver(post_save,sender=Buyer)
def create_cart(instance,*args, **kwargs):
    if not Cart.objects.filter(buyer=instance).exists():
        Cart.objects.create(buyer=instance)