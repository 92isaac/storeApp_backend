from django.contrib import admin
from .models import Product, Cart, Cartitems, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Cartitems)