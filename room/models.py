from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    """Model definition for chat room."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        """Unicode representation of Room."""
        return self.name


class Message(models.Model):
    """Model definition for Message."""

    room = models.ForeignKey(Room, related_name="message", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="message", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_added",)

    def __str__(self):
        """Unicode representation of Message."""
        return self.content
