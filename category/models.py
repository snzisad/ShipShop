from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField()

    def __self__(self):
        return self.name
