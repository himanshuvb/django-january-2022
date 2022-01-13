from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def music_home(request):
	return HttpResponse("<h1>It works !</h1>")


def songs_list(request):
	songs = ['song1', 'song2', 'song3', 'song4', 'song5', 'song6']
	output = ""
	for song in songs:
		output += song + "<br>"
	return HttpResponse("<h1>THIS IS A LIST OF SONGS</h1><br>" + output)


