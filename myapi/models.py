from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)

# Create your models here.
def __str__(self) ->str:
    return self.name

