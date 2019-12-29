from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.views import generic, View
from qa.models import Question,Answer
from django.views import generic
class IndexView(generic.ListView):
    model = Question
    template_name='qa/index.html'
    context_object_name='new_question_list'
    paginate_by=10
    def get_queryset(self):
        qs=Question.objects.new()
        return qs
class PopularView(generic.ListView):
    model=Question
    template_name='qa/popular_questions.html'
    context_object_name='popular_question_list'
    paginate_by=10
    def get_queryset(self):
        return Question.objects.popular()
class DetailQuestionView(generic.DetailView):
    model=Question
    template_name='qa/question_detail.html'
    
