from __future__ import unicode_literals
from django.db import models
from account.models import Client
from core.helpers.model import TimeStamp

Type_Choice = (
    ('center_distribution', u'center_distribution'),
    ('branch', u'branch'),
    ('associated_company', u'associated_company'),
)


class Provider(TimeStamp):
    name = models.CharField(max_length=100, blank=True)
    address = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(TimeStamp):
    code = models.CharField(max_length=50, blank=True, unique=True)
    description = models.TextField()
    provider = models.ManyToManyField(Provider)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.code


class Order(TimeStamp):
    client = models.ForeignKey(Client, related_name='order_client', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.SET_NULL, null=True)
    assortment = models.DateTimeField(auto_now=False, blank=True, null=True)
    urgent = models.BooleanField(default=False)
    type = models.CharField(max_length=100, blank=True, choices=Type_Choice, default='center_distribution')
    warehouse = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    detail = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id


