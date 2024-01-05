from django.db import models

# Create your models here.
class Solar(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
    add_desc = models.CharField(max_length=155)


