from tkinter import CASCADE
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    new_artist_name = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    album_art_url = models.CharField(max_length=1023, blank=True, null=True)
    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums", blank=True, null=True)

    def __str__(self) -> str:
        return self.title
