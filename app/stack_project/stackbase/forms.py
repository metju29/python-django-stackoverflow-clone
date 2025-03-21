from .models import Comment, Question
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditor5Widget(config_name='default'),
        }

        labels = {
            'title': 'Title',
            'content': 'Question'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditor5Widget(config_name='default')
        }

        labels = {
            'name': 'Name',
            'content': 'Comment'
        }