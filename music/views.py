from django.shortcuts import render, redirect, get_object_or_404
from .forms import TrackForm
from .models import Track
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from pygame import mixer


def create_track(request):
    if request.user.is_admin is True:
        if request.method == 'POST':
            form = TrackForm(request.POST, request.FILES)
            if form.is_valid():
                track = form.save(commit=False)
                track.artiste = request.user
                track.save()
                return redirect('home')
        else:
            form = TrackForm()
        context = {
            'form': form
        }
        return render(request, 'createTrack.html', context)
    else:
        raise PermissionDenied


def edit_track(request, pk):
    if request.user.is_admin is True:
        track = get_object_or_404(Track, pk=pk)
        if request.method == 'POST':
            form = TrackForm(request.POST, instance=track)
            if form.is_valid():
                track = form.save(commit=False)
                track.artiste = request.user
                track.save()
                return redirect('allTracks')
        else:
            form = TrackForm(instance=track)
        context = {
            'form': form
        }
        return render(request, 'allTracks.html', context)
    else:
        raise PermissionDenied


def delete_track(request, pk):
    if request.user.is_admin is True:
        track = get_object_or_404(Track, pk=pk)
        track.delete()
        context = {
            'track': track
        }
        return render(request, 'viewTrack.html', context)
    else:
        raise PermissionDenied


def play_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    mixer.init()
    mixer.music.load(track.song)
    mixer.music.set_volume(0.5)
    mixer.music.play()
    track.is_playing = True
    track.listen_count += 1
    track.save()
    context = {
        'track': track
    }
    return render(request, 'viewTrack.html', context)


def stop_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    mixer.init()
    mixer.music.load(track.song)
    mixer.music.stop()
    track.is_playing = False
    track.save()
    context = {
        'track': track
    }
    return render(request, 'viewTrack.html', context)


def pause_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    mixer.init()
    mixer.music.load(track.song)
    mixer.music.pause()
    track.is_playing = False
    track.save()
    context = {
        'track': track
    }
    return render(request, 'viewTrack.html', context)


def unpause_track(request, pk):
    track = get_object_or_404(Track, pk=pk)
    mixer.init()
    mixer.music.load(track.song)
    mixer.music.unpause()
    track.is_playing = False
    track.save()
    context = {
        'track': track
    }
    return render(request, 'viewTrack.html', context)


def home(request):
    tracks = Track.objects.all().order_by('-date_posted').select_related('artiste')
    try:
        track = Track.objects.get(is_playing=True)
        mixer.init()
        mixer.music.load(track.song)
        mixer.music.stop()
        track.is_playing = False
        track.save()
    except Track.DoesNotExist:
        paginator = Paginator(tracks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'allTracks.html', context)
    paginator = Paginator(tracks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'allTracks.html', context)


def is_like(request, pk):
    track = get_object_or_404(Track, pk=pk)
    track.is_liked = True
    track.save()
    return redirect('home')


def is_unlike(request, pk):
    track = get_object_or_404(Track, pk=pk)
    track.is_liked = False
    track.save()
    return redirect('home')


