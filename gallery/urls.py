from django.urls import path
from .views import album_list, album_detail
from . import views
from gallery import views

urlpatterns = [
    path('albuns/', album_list, name='album_list.html'),
    path('albuns/<int:album_id>/', album_detail, name='album_detail'),
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    
]
