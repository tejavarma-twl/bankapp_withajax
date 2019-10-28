from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.BigIntegerField()
    address = models.TextField(default='')
    bank    = models.CharField(default='',max_length=20)
    account = models.CharField(default='',max_length=12)
    balance = models.BigIntegerField(default=500000)

class Transactions(models.Model):
    user = models.ManyToManyField(User)
    trans_date = models.DateField(auto_now=False, auto_now_add=False)
    to_user = models.BigIntegerField()
    amount = models.FloatField(default=0)

class BankDetails(models.Model):
    bank_name = models.CharField(default='',max_length=20)
    bank_branch = models.CharField(default='',max_length=20)
    bank_branchcode = models.CharField(default='',max_length=20)
    bank_ifsc  = models.CharField(default='',max_length=20) 

class AddBen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beneficiary_name    = models.CharField(default='',max_length=30)
    beneficiary_accno   = models.BigIntegerField(null=True, blank= True)
    ifsc_code           = models.CharField(default='',max_length=20)