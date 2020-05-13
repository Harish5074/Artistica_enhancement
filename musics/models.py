from django.db import models


class Album(models.Model):
    class Meta:
        db_table = "musics"

    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)

    def __str__(self):
        return self.album_title + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title + "." + self.file_type

# Create your models here.
