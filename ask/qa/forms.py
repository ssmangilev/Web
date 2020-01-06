from django import forms
from qa.models import Question,Answer,Session,CustomUser
from django.core.exceptions import ValidationError

class SignupForm(forms.Form): # form for signup
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField()
    def save(self):
        return CustomUser.objects.create(login=self.cleaned_data['username'],password=self.cleaned_data['password'],email=self.cleaned_data['email'])

class AskForm(forms.Form): # Form for creating new Question
    title=forms.CharField(max_length=100)
    text=forms.CharField(widget=forms.Textarea)
    def save(self):
        new_question=Question.objects.create(title=self.cleaned_data['title'],text=self.cleaned_data['text'],author_id=self._user)
        return new_question


class AnswerForm(forms.Form): # form for creating new Answer
    text=forms.CharField(max_length=1000)
    question=forms.IntegerField()
    def save(self):
         
        new_answer=Answer.objects.create(text=self.cleaned_data['text'],question_id=self.cleaned_data['question'],author_id=self._user)
        return new_answer
class LoginForm(forms.Form): # form for login
    login=forms.CharField(max_length=100)
    password=forms.CharField()
    
