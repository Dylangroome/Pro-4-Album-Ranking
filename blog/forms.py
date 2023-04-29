
from .models import Album, Comment, RATE_CHOICES
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rate')

