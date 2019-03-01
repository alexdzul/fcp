from django.db import models

# Create your models here.

class email(models.Model):
    email = models.EmailField(max_length=70, blank=True)

class Whoweare(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=1000)
