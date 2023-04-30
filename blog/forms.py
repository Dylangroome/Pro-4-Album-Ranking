
from .models import Album, Comment, RATE_CHOICES
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rate')
        labels = {
            "body": "Share your idea on this ticker",
        }


class EditForm(forms.ModelForm):
    '''
    Form to edit the body of a comment
    and change ratings
    '''
    class Meta:
        """
        Link for to model, set fields and labels
        """
        model = Comment
        fields = ('body', 'rate')
        labels = {
            "body": "Post a comment:",
            "rate": "Change your rating:"
        }
