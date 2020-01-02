from django import forms
from .models import Question,Answer
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AskForm(forms.Form): # Form for creating new Question
    title=forms.CharField(max_length=100)
    text=forms.CharField(widget=forms.Textarea)
    def save(self):
        user=User.objects.get(pk=1)
        new_question=Question.objects.create(title=self.cleaned_data['title'],text=self.cleaned_data['text'],author=user)
        return new_question


class AnswerForm(forms.Form):
    text=forms.CharField(max_length=1000)
    question=forms.ModelChoiceField()
    def save(self):
        user=User.objects.get(pk=1)
        new_answer=Answer.objects.create(text=self.cleaned_data['text'],question=self.cleaned_data['question'],author=user)
        return new_answer
