from tkinter import CASCADE
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    album_art_url = models.CharField(max_length=1023, blank=True, null=True)
    artist_other = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums", blank=True, null=True)

    def __str__(self) -> str:
        return self.title
