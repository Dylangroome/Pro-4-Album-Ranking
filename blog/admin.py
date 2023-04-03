from django.contrib import admin
from .models import Album, Genre, Artist, Rating

admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Rating)