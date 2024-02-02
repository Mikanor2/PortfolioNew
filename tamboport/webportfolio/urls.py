from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
    path('Home/', views.Home, name="Home"),
    path('About/', views.About, name="About"),
    path('Info/', views.Info, name="Info")
]