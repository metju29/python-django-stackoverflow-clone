from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Question, Comment
from .forms import CommentForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# CRUD function
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'content']

    def test_func(self):
        return self.get_object().user == self.request.user

class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name = 'question'
    success_url = reverse_lazy('stackbase:question-list')

    def test_func(self):
        return self.get_object().user == self.request.user

class CommentDetailView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('stackbase:question-detail')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_answer.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('stackbase:question-detail', kwargs={'pk': self.kwargs['pk']})

