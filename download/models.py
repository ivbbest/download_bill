from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Organization(models.Model):
    client_name = models.ForeignKey('Client', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=255)


class Bill(models.Model):
    client_name = models.ForeignKey('Client', on_delete=models.CASCADE)
    client_org = models.ForeignKey('Organization', on_delete=models.CASCADE)
    number = models.IntegerField()
    sum = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField()
    service = models.TextField()
