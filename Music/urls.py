from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_home, name="music_home"),
    path('songs/', views.songs_list, name="songs_list")
]
