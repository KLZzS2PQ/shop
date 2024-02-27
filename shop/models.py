from django.db import models


class Rarity(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/images/')
    price = models.FloatField()
    desc = models.TextField()
    rating = models.FloatField()
    discount = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    rarity = models.ForeignKey(to='Rarity', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    delivery_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
