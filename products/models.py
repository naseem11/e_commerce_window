from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        app_label='products'
    name=models.CharField(max_length=250,default='')
    description=models.TextField()
    price=models.DecimalField( max_digits=6 ,decimal_places=2,)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name
