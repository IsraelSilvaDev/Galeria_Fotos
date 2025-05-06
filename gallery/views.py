from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album, Foto
from django.contrib.auth import authenticate, login
from django.contrib import messages
def album_list(request):
    albuns = Album.objects.all()
    return render(request, 'gallery/album_list.html', {'albuns': albuns})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    fotos = album.fotos.filter(aprovado=True)
    return render(request, 'gallery/album_detail.html', {'album': album, 'fotos': fotos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect('home')
            return('home.html')  # redireciona para a página principal após login

        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')




