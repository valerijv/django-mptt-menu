# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel, TreeForeignKey


@python_2_unicode_compatible
class Category(MPTTModel):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    parent = TreeForeignKey('self',
                            db_index=True,
                            on_delete=models.CASCADE,
                            related_name='categories',
                            null=True,
                            blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=16,
                                decimal_places=2)
    parent = models.ForeignKey(Category,
                               db_index=True,
                               related_name='products',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'
