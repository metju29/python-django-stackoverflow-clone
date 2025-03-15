from django.shortcuts import render
from django.views.generic import ListView
from .models import Question


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# CRUD function
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']
