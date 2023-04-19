from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

GENRE_CHOICES = ((1, "HipPop"), (2, "RnB"))

RATE_CHOICES = (
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
)


class Artist(models.Model):
    name = models.CharField(max_length=70, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    year = models.CharField(max_length=25, blank=True)
    rated = models.CharField(max_length=10, blank=True)
    released = models.CharField(max_length=25, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    genre = models.PositiveSmallIntegerField(choices=GENRE_CHOICES, default=1)
    artist = models.ManyToManyField(Artist, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=7)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title