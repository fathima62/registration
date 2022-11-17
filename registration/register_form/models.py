from django.db import models

# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    postcode = models.IntegerField()
    purpose = models.CharField(max_length=200)
    amount = models.BigIntegerField()
    asset_cost = models.BigIntegerField()
    tentor = models.BigIntegerField()
    tentormonthly = models.BigIntegerField()
    photo = models.ImageField(upload_to='form/',default='')
    document = models.ImageField(upload_to='form/',default='')