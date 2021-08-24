from django.contrib.auth.models import User
from django.db import models
from velo.models import Marsh
from django.conf import settings
from django.db import models



# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart_id = models.CharField(max_length=250, blank=True)
    cart_added = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['cart_added']
        db_table = 'Cart'


class CartItem(models.Model):
    product = models.ForeignKey(Marsh, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CartItem'
