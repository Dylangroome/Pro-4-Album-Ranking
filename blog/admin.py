from django.contrib import admin
from .models import Album
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Album)
class AlbumAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')