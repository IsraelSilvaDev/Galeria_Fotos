from django.urls import path
from .views import album_list, album_detail

urlpatterns = [
    path('albuns/', album_list, name='album_list'),
    path('albuns/<int:album_id>/', album_detail, name='album_detail'),
]
