from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return f"#{self.title}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='groups/', null=True, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='meme_groups')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Meme(models.Model):
    CONTENT_TYPES = [
        ('IMG', 'Image'),
        ('VID', 'Video'),
        ('TXT', 'Text meme'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True)
    content_type = models.CharField(max_length=3, choices=CONTENT_TYPES, default='IMG')
    
    file = models.FileField(upload_to='memes/%Y/%m/', null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='memes')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    
    tags = models.ManyToManyField(Tag, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    total_rating = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['-created_at'] 

class Comment(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    VOTE_CHOICES = [
        (1, 'Upvote'),
        (-1, 'Downvote'),
        (5, 'Meme Buddy')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'meme')