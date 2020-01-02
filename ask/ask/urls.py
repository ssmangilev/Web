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
from . import views
import re
urlpatterns = [
    path('',include('qa.urls')),
    path('admin/', admin.site.urls),
    path('login/',views.testView),
    path('signup/',views.testView),
    #path('question/<int:id>/',views.testView),
    #path('ask/',include('qa.urls',namespace='qa:question_create_url')),
    #path('popular/',views.testView),
    #path('new/',views.testView),
    path('qa/',include('qa.urls'))
]
