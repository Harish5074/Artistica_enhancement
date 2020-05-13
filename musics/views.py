from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# from django.template import loader
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'musics/index.html', {'all_albums': all_albums})
# Create your views here.


def details(request, album_id):
    try:
        album = Album.objects.get(id= album_id)
    except Album.DoesNotExist:
        raise Http404("The album dies not exist")
    return render(request, 'musics/detail.html', {'album': album})
