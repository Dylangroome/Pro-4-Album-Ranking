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


# class PostTemplateView(TemplateView):
#     '''
#     For the post page url
#     '''
#     template_name = 'post.html'


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

            },
        )

    # def post(self, request, slug, *args, **kwargs):

    #     queryset = Album.objects.filter(status=1)
    #     album = get_object_or_404(queryset, slug=slug)
    #     questions = post.questions.filter(approved=True).order_by("-created_on")  # noqa
    #     enrolled = False
    #     if post.no_participants.filter(id=self.request.user.id).exists():
    #         enrolled = True
    #     question_form = QuestionForm(data=request.POST)
    #     if question_form.is_valid():
    #         question_form.instance.email = request.user.email
    #         question_form.instance.name = request.user.username
    #         question = question_form.save(commit=False)
    #         question.post = post
    #         question.save()
    #     else:
    #         question_form = QuestionForm()

    #     return render(
    #         request,
    #         "post_detail.html",
    #         {
    #             "post": post,
    #             "questions": questions,
    #             "asked": True,
    #             "question_form": question_form,
    #             "enrolled": enrolled,
    #         },
    #     )