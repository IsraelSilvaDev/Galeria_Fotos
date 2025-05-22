from django.urls import path
from django.views.generic import TemplateView   
from .views import album_list, album_detail
from . import views
from gallery import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index'), name='index'), 
    path('albuns/', views.album_list, name='album_list'),
    path('albuns/<int:album_id>/', album_detail, name='album_detail'),
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),    
    path('buttons/', views.buttons_view, name='buttons'),
    path('', views.photo_upload_view, name='photo_upload'),
    path('logout/', views.logout_view, name='logout'),
    
]