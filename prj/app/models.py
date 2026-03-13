from django.db import models

# Create your models here.

class Meme(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True)
    user = models.ForeignKey('user', null=True, on_delete=models.SET_NULL)
class user(models.Model):
    username = models.CharField
