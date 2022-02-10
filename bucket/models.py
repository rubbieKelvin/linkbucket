import uuid
from django.db import models

class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

class Link(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    link = models.URLField()
    image = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    author = models.ForeignKey('authr.User', related_name='links', on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag, related_name='links')
    trackable_link = models.CharField(max_length=100)

class Bookmark(models.Model):
    id = models.BigAutoField(primary_key=True)
    link = models.ForeignKey(Link, related_name='bookmarks', on_delete=models.CASCADE)
    user = models.ForeignKey('authr.User', related_name='bookmarks', on_delete=models.CASCADE)

class Vote(models.Model):
    class Type(models.TextChoices):
        UPVOTE = "UPVOTE"
        DOWNVOTE = "DOWNVOTE"

    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    type = models.CharField(max_length=8, choices=Type.choices)
    user = models.ForeignKey('authr.User', on_delete=models.CASCADE, related_name='votes')
    date_voted = models.DateTimeField(auto_now_add=Type)
