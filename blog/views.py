from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from .models import Album, Artist
from .forms import CommentForm


class AlbumList(generic.ListView):
    model = Album
    queryset = Album.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class AboutTemplateView(TemplateView):
    '''
    For the about page url
    '''
    template_name = 'about.html'


class Page403(TemplateView):
    '''
    For the 403 page url
    '''
    template_name = '403.html'


class Page404(TemplateView):
    '''
    For the 404 page url
    '''
    template_name = '404.html'


class Page500(TemplateView):
    '''
    For the 500 page url
    '''
    template_name = '500.html'


# class CreateMyModelView(View):
#     model = Album
#     form_class = MyModelForm


class AlbumDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Album.objects.filter(status=1)
        album = get_object_or_404(queryset, slug=slug)
        comments = album.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "post.html",
            {
                "album": album,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm

            },
        )
    
    def album(self, request, slug, *args, **kwargs):

        queryset = Album.objects.filter(status=1)
        album = get_object_or_404(queryset, slug=slug)
        comments = album.comments.filter(approved=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.album = album
            comment.save()
        else:
            comment_form = CommentForm()
        
        rate_form = RateForm(data=request.POST)
        if rate_form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.album = album
            rate.save()
        else:
            rate_form = RateForm()

        return render(
            request,
            "post.html",
            {
                "album": album,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


class ArtistDetail(View):
    
    def artist(request, artist_slug):
        artist = get_object_or_404(Artist, slug=artist_slug)
        album = Album.objects.filter(Artist=artist)
        comments = album.comments.filter(approved=True).order_by("-created_on")

        context = {
            'album': album,
            'artist': artist,
            "commented": False,
        }
        template = loader.get_template('about.html')

        return HttpResponse(template.render(context, request))
    
    
