# app/models.py

from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)

    def __str__(self):
        return self.field1
