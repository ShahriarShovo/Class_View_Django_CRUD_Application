from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

# Create your models here.

class Employee_List_Database(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    address=models.TextField()
    phone=models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('crud:index')

