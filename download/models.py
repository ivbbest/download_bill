from datetime import datetime

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    client_name = models.CharField(max_length=100)
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bill(models.Model):
    client_name = models.CharField(max_length=100)
    client_org = models.CharField(max_length=150)
    number = models.IntegerField()
    sum = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(null=True, blank=True)
    service = models.TextField()
    fraud_score = models.CharField(max_length=100, null=True, blank=True)
    service_class = models.CharField(max_length=100, null=True, blank=True)
    service_name = models.CharField(max_length=100, null=True, blank=True)
