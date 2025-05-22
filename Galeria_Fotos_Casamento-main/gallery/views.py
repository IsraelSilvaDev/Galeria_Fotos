from django.shortcuts import render, get_object_or_404
from .models import Album, Foto

def album_list(request):
    albuns = Album.objects.all()
    return render(request, 'gallery/album_list.html', {'albuns': albuns})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    fotos = album.fotos.filter(aprovado=True)
    return render(request, 'gallery/album_detail.html', {'album': album, 'fotos': fotos})
