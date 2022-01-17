from django.http import HttpResponse
from django.shortcuts import render
from .models import Song, Album

# Create your views here.
def music_home(request):
	return HttpResponse("<h1>It works !</h1>")


def songs_list(request):
	songs = Song.objects.all()
	output = ""
	for song in songs:
		output += str(song) + "<br>"
	return HttpResponse("<h1>THIS IS A LIST OF SONGS</h1><br>" + output)



def album_list(request):
	album_list = Album.objects.all()
	output = ""
	for album in album_list:
		output += str(album) + "<br>"
	return HttpResponse("<h1>THIS IS A LIST OF ALBUMS</h1><br>" + output)


