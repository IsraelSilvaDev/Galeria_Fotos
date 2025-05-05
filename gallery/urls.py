from django.urls import path
from .views import album_list, album_detail
from . import views

urlpatterns = [
    path('', album_list, name='album_list'),
    path('albuns/<int:album_id>/', album_detail, name='album_detail'),
    path('login/', views.login_view, name='login'),
]
