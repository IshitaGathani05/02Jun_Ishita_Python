from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# Class
class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=255, null=True, blank=True)

'''class OTP(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def is_valid(self):
        return timezone.now() <= self.created_at + datetime.timedelta(minutes=2)'''


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", null=True, blank=True)  # optional image
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name 