from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views
from myapp import signals

app_name = "myapp" 

urlpatterns = [
    path('', views.home, name='home'),
    #path('courses/', include('courses.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout, password reset
    
]

from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)