from django.db import models
from django.conf import settings


class Track(models.Model):
    title = models.CharField(max_length=100)
    artiste = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.FileField(upload_to='songs')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_liked = models.BooleanField(default=False)
    listen_count = models.PositiveIntegerField(default=0)
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return self.title