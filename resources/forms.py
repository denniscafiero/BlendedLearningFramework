from django import forms

from .models import Resource, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('title', 'content',)