
from .models import Album, Comment, RATE_CHOICES
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rate')


# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = ['rate',]


# class RateForm(forms.ModelForm):
#     rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

#     class Meta:
#         model = Album
#         fields = ('rate',)
