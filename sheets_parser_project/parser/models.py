from django.db import models

# Create your models here.
class OrderModel(models.Model):
    order_number = models.CharField(max_length=250)
    price_usd = models.IntegerField()
    price_rub = models.IntegerField()
    order_date = models.DateTimeField()

