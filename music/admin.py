from django.contrib import admin
from music.models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_posted', 'title', 'is_liked',)


admin.site.register(Track, TrackAdmin)