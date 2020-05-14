from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album
# from django.template import loader
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'musics/index.html', {'all_albums': all_albums})
# Create your views here.


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'musics/detail.html', {'album': album})
