from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gallery.models import Album, Foto
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms # Certifique-se de que este formulário está definido em gallery/forms.py


def album_list(request):
    albuns = Album.objects.all()
    return render(request, 'album_list.html', {'albuns': albuns})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    fotos = album.fotos.filter(aprovado=True)
    return render(request, 'album_detail.html', {'album': album, 'fotos': fotos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('buttons')  # redireciona para a view principal
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

def home_view(request):
    return redirect('album_list')

def buttons_view(request):
    return render(request, 'buttons.html')

def photo_upload_view(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.user = request.user
            foto.save()
            messages.success(request, 'Foto enviada com sucesso!')
            return redirect('album_list')  # Redireciona após o upload bem-sucedido
    else:
        form = FotoForm()
    return render(request, 'photo_upload.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('album_list')  # Redireciona após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




