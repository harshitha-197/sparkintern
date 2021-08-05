from django.db import models

class customerdata(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True,blank=False)
    mobile = models.BigIntegerField(unique=True,blank=False)
    account_number = models.BigIntegerField()
    balance = models.BigIntegerField()

class transfer(models.Model):
    fromaccount = models.BigIntegerField(verbose_name="From Account")
    toaccount = models.BigIntegerField(verbose_name="To Account")
    amount = models.BigIntegerField(verbose_name="Amount")

