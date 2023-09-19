from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Account(models.Model):
    SAVINGS = 'S'
    CURRENT = 'C'
    FIXED = 'F'
    RECURRING = 'R'
    TYPE_CHOICES = [
        (SAVINGS, 'Savings'),
        (CURRENT, 'Current'),
        (FIXED, 'Fixed'),
        (RECURRING, 'Recurring')
    ]

    number = models.CharField(max_length=15)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=SAVINGS)
    balance = models.FloatField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def get_type(self):
        if self.type == self.SAVINGS:
            return 'Savings'
        elif self.type == self.RECURRING:
            return 'Recurring'
        elif self.type == self.CURRENT:
            return 'Current'
        else:
            return 'Fixed Deposit'


class Transaction(models.Model):
    DEPOSIT = 'D'
    WITHDRAWAL = 'W'
    TRANSFER = 'T'
    MODE_CHOICES = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal'),
        (TRANSFER, 'Transfer')
    ]

    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    description = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=1, choices=MODE_CHOICES, default=TRANSFER)
    payee = models.ForeignKey(Customer, on_delete=models.PROTECT)
    receiver = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='+')





