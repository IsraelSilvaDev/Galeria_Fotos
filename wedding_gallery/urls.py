from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gallery import views
from django.views.generic import TemplateView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.login_view, name='login'),
    path('', views.buttons_view, name='buttons'),
    
    
    path('home/', views.home_view, name='home'),
   
    path('photo_upload/', views.photo_upload_view, name='photo_upload'),
    path('index/', TemplateView.as_view(template_name='index'), name='index'), 
    path('', include('gallery.urls')),  
     # Página inicial
]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
