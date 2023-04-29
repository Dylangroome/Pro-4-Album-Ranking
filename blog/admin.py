from django.contrib import admin
from .models import Album, Comment, Artist
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Album)
class AlbumAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Add the comment models to the admin panel
    apply summernote to the comment text field
    add approved/not approved filters and serach
    functionalities
    '''
    list_display = ('name', 'body', 'rate', 'album',
                    'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        '''
        Give the admin the possibility to approve
        comments
        '''
        queryset.update(approved=True)


@admin.register(Artist)
class ArtistAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)