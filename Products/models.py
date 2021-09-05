from django.db import models
from django.contrib.auth.models import User


class Product1(models.Model):
    prod_choices = (
        ("Mobile", "Mobile"),
        ("Tablet", "Tablet"),
        ("Desktop", "Desktop"),
        ("Laptop", "Laptop"),
    )
    prod1 = models.CharField(
        max_length=40, choices=prod_choices, null=False, blank=False,)
    Name = models.CharField(max_length=40, null=False, blank=False)
    screensize = models.DecimalField(
        max_digits=6, blank=True, decimal_places=2)
    price = models.FloatField(default=0.0)
    brand = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField("TYPE YOUR DESCRIPTION", null=True)
    quantity = models.IntegerField(default=0)
    battery = models.CharField(default='None', max_length=40)
    status = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='media/mobile/images', default="media/mobile/images/default_m.jpg")
    dealerQuantity = models.IntegerField(default=1)
    delivery = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=4, default=0, decimal_places=1)
    display = models.CharField(max_length=20, default='HD')
    frontCamera = models.IntegerField(null=False)
    rearCamera = models.IntegerField(null=False)
    waterproof = models.BooleanField(default=False)
    goodies = models.CharField(max_length=50, default='Guide')
    Refurbished = models.BooleanField(default=False)
    os = models.CharField(max_length=10, default='Android')

    def __str__(self):
        return self.Name


class shop(models.Model):
    name = models.OneToOneField(to=User, on_delete=models.CASCADE, null=False)
    prod = models.ManyToManyField(to=Product1, related_name="prod", null=True)
    orders = models.IntegerField(default=0)
    rating = models.FloatField(default=5)
    location = models.TextField(default="India")
    contact = models.CharField(max_length=13, default="+91")

    def __str__(self):
        return self.name


'''class customer(models.Model):
    name = models.OneToOneField(to=User, on_delete=models.CASCADE,)
    product = models.ManyToManyField()
    dealer_name = models.ManyToManyField(
        to=shop.name, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField()
    prod = models.ManyToManyField(to=Product1, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name


class cart(models.Model):
    name = models.OneToOneField()'''
