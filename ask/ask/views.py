from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.views.generic import View
from qa.forms import *

def testView(request,*args,**kwargs):
    try:
        return HttpResponse('OK')
    except:
        raise Http404
