from django.db import models


class Customer(models.Model):
    c_id = models.IntegerField(unique=True)
    f_name = models.CharField(max_length=60)
    l_name = models.CharField(max_length=60)
    product = models.CharField(max_length=70)
    price = models.IntegerField()
