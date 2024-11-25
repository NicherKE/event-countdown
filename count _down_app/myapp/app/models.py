from django.db import models
from django.contrib import admin

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=255)
