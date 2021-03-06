"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from qa import views
import re
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('new/',views.IndexView.as_view(),name='new'),
    path('popular/',views.PopularView.as_view(), name='popular'),
    path('question/<int:pk>/',views.DetailQuestionView.as_view(),name='question_detail_view'),
    path('ask/',views.QuestionCreateView.as_view(),name='question_create_url'),
    path('ask',views.QuestionCreateView.as_view(),name='question_create_url'),
    path('',views.IndexView.as_view(), name='index'),
]
