from django.db import models
from core import settings
# Create your models here.


class OrderModel(models.Model):

    order_number = models.CharField(max_length=250)
    price_usd = models.IntegerField()
    order_date = models.CharField(max_length=11)
    price_rub = models.FloatField()
