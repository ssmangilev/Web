from django.db import models
from django.urls import reverse
from django.utils import timezone
import random
import string
import datetime
class CustomUserManager(models.Manager):
    def do_login(self,login,password):
        try:
            user = CustomUser.objects.get(login=login)
        except CustomUser.DoesNotExist:
            return None
        if password != user.password:
            return None
        session=Session()
        session.key=Session.objects.randomize_key()
        session.user=user
        session.expires=timezone.datetime.now()+timezone.timedelta(days=5)
        session.save()
        return session.key
class CustomUser(models.Model):
    login = models.CharField(unique=True,max_length=100)
    password = models.CharField(max_length=100)
    email=models.EmailField()
    objects=CustomUserManager()
class SessionManager(models.Manager):
    def randomize_key(self): # method for generate auth cookie
        token=''
        for i in range (40):
            token+=random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)
        return token
class Session(models.Model):
    key=models.CharField(unique=True,max_length=255)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    expires=models.DateTimeField()
    objects=SessionManager()
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
    author=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)
    likes=models.ManyToManyField(CustomUser,related_name='question_like_user')
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
    author=models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.text
