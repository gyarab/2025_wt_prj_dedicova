from django.contrib import admin
from .models import Meme, Tag, Group, Comment, Vote
# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'group', 'content_type', 'total_rating', 'display_tags', 'created_at']
    
    list_filter = ['content_type', 'group', 'created_at']
    
    search_fields = ['title', 'description', 'user__username']
    
    filter_horizontal = ['tags']

    def display_tags(self, obj):
        return ", ".join([t.title for t in obj.tags.all()])
    display_tags.short_description = 'Tags'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'meme', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'user__username']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'meme', 'value']
