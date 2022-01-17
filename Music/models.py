from django.db import models


# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	genre = models.CharField(max_length=50)
	rating = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id) + " - " + self.title


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	lyrics = models.CharField(max_length=5000)

	def __str__(self):
		return self.album.title + " - " + self.name
'''

1> python code -> models.py

2> python manage.py makemigrations
migrations/0001_initals.py -> intermediate file 

3> python manage.py migrate
This will convert our python code in migrations folder to SQL code and run it 

'''