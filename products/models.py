from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=20, verbose_name='거래처명')
    phone = models.CharField(max_length=20, verbose_name='전화번호')
    address = models.CharField(max_length=100, verbose_name='주소')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='제품명')
    image = models.ImageField(blank=True)
    detail = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    remaining = models.PositiveIntegerField(default=0)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name