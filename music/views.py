from django.shortcuts import render, get_object_or_404
from .models import Album

#music -> templates -> music -> index.html

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/pages/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/pages/detail.html', {'album': album})