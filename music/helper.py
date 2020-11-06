# Music player in python

from pygame import mixer
from django.shortcuts import get_object_or_404
from music.models import Track


def play_music(track):
    mixer.init()
    mixer.music.load(track.song)
    mixer.music.set_volume(1)
    mixer.music.play()