from django.contrib import admin
from .models import Meme, user

# Register your models here.

@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display=['title']
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    pass