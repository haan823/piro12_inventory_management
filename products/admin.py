from django.contrib import admin

# Register your models here.
from products.models import Seller, Product

admin.site.register(Seller)

admin.site.register(Product)