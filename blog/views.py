from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from .models import Album


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


class ContactTemplateView(TemplateView):
    '''
    For the contact page url
    '''
    template_name = 'contact.html'


class PostTemplateView(TemplateView):
    '''
    For the post page url
    '''
    template_name = 'post.html'


# class PostDetail(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Album.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "post.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "liked": liked
#             },
#         )