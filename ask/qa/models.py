from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=255)
    text=models.CharField(max_length=2000)
    added_at=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    likes=models.ManyToManyField(User,related_name='question_like_user')
    objects=QuestionManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # write path to url name as app.name:url_pattern_name if app isnt root
        return reverse ('question_detail_view',args=[self.id])

class Answer (models.Model):
    text=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.text
