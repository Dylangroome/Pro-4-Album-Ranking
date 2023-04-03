from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Genre(models.Model):
	title = models.CharField(max_length=25)
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return self.name


class Artist(models.Model):
	name = models.CharField(max_length=70, unique=True)
	featured_image = CloudinaryField('image', default='placeholder')
	slug = models.SlugField(max_length=200, unique=True)
	
	def __str__(self):
		return self.name


class Rating(models.Model):
	source = models.CharField(max_length=50)
	rating = models.CharField(max_length=10)

	def __str__(self):
		return self.source


class Album(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	year = models.CharField(max_length=25, blank=True)
	rated = models.CharField(max_length=10, blank=True)
	released = models.CharField(max_length=25, blank=True)
	genre = models.ManyToManyField(Genre, blank=True)
	artist = models.ManyToManyField(Artist, blank=True)
	featured_image = CloudinaryField('image', default='placeholder')
	ratings = models.ManyToManyField(Rating, blank=True)

	def __str__(self):
		return self.Title


RATE_CHOICES = [
	(1, '1 - Burn it'),
	(2, '2 - Mute'),
	(3, '3 - Terrible'),
	(4, '4 - Bad'),
	(5, '5 - OK'),
	(6, '6 - Listenable'),
	(7, '7 - Good'),
	(8, '8 - Recommended'),
	(9, '9 - Perfect'),
	(10, '10 - Master Piece'), 
]


class Comment(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="comments")
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	class Meta:
		ordering = ["created_on"]

	def __str__(self):
		return f"Comment {self.body} by {self.name}"