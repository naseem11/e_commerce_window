from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=250,default='')
    description=models.TextField()
    price=models.DecimalField( max_digits=6 ,decimal_places=2,)
    def __str__(self):
        return self.name
