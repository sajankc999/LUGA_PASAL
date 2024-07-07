from django.contrib import admin
from .models import *
# Register your models here.

class ProductModel(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    exclude = ('slug',)
    list_display=['title','category']

admin.site.register(Product,ProductModel)



admin.site.register(Category)
admin.site.register(Targeted_age)
admin.site.register(Size)