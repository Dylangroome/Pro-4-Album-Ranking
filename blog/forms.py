
from .models import Album, Comment, RATE_CHOICES
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rate')


class EditForm(forms.ModelForm):
    '''
    Form to edit the body of a comment
    and change sentiment
    '''
    class Meta:
        """
        Link for to model, set fields and labels
        """
        model = Comment
        fields = ('body', 'rate')
        labels = {
            "body": "Post a comment:",
            "rate": "Change your sentiment:"
        }
