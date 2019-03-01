from django.db import models

# Create your models here.

class Contact (models.Model):
    email = models.EmailField(max_length=70, blank=True)
    comentario = models.TextField(max_length=1000, null=True, blank=True)


class Whoweare(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=1000)

class Ourhistory(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
