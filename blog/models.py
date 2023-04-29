from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


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
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(null=True, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('artist', args=[self.slug])


class Album(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    year = models.CharField(max_length=25, blank=True)
    rated = models.CharField(max_length=10, blank=True)
    released = models.CharField(max_length=25, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=1)
    artist = models.ManyToManyField(Artist, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
           
    
class Comment(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE,
                              related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    rate = models.CharField(max_length=6, choices=RATE_CHOICES, default=7)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


