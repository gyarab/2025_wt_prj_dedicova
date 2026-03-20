from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Meme(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True, max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField
    tag = models.ForeignKey('Tag', null=True, on_delete=models.SET_NULL)
    
class Tag(models.Model):
    title = models.CharField(max_length=255)
