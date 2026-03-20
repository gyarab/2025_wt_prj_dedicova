from django.contrib import admin
from .models import Meme, Tag

# Register your models here.


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display=['title', 'description', 'user', 'rating', 'tag']
    search_fields=['title']
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['title']
    search_fields=['title']
