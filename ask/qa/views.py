from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from django.views import generic, View
from qa.models import Question,Answer
from django.views import generic
from qa.forms import *
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
class DetailQuestionView(generic.View):
    #model=Question
    #template_name='qa/question_detail.html'
    def get(self, request, pk):
        form = AnswerForm()
        qs=Question.objects.get(pk=pk)
        return render (request, 'qa/question_detail.html', context={'form':form,'question':qs})
class QuestionCreateView(generic.View):
    def get(self, request):
        form = AskForm()
        return render (request, 'qa/question_create.html', context= {'form': form})
    def post(self,request):
        bound_form=AskForm(request.POST)
        if bound_form.is_valid():
            new_question=bound_form.save()
            return redirect(new_question)
        return render(request,'qa/question_create.html',context={'form':bound_form})
