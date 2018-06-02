# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from menu.models import Category, Product
from faker import Faker
from random import randint


class Command(BaseCommand):
    help = '''
        Generates random initial categories and products
        categories count = spread ^ max_depth
        products count = spread ^ max_depth * max_products / 2
    '''

    def __init__(self, *args, **kwargs):
        self.fake = Faker()
        self.max_depth = 4
        self.spread = 5
        self.max_products = 20
        self.bulk_products = []
        super(Command, self).__init__(*args, **kwargs)

    def get_category(self, parent):
        category = Category(
            name=self.fake.company(),
            active=True,
            parent=parent
        )
        category.save()
        return category

    def get_product(self, category):
        product = Product(
            name=self.fake.name(),
            price=randint(1, 99),
            active=True,
            parent=category
        )
        self.bulk_products.append(product)
        return product

    def tree(self, category, depth):
        if depth < self.max_depth:
            depth += 1
            for i in range(1, self.spread):
                new_category = self.get_category(category)
                self.tree(new_category, depth)
        else:
            return

    def fill_with_products(self):
        for category in Category.objects.all():
            for p in range(0, randint(0, self.max_products)):
                self.get_product(category)

    def handle(self, *args, **options):
        for i in range(1, self.spread):
            category = self.get_category(None)
            self.tree(category, 0)

        self.fill_with_products()
        Product.objects.bulk_create(self.bulk_products)

        self.stdout.write(self.style.SUCCESS('Done'))