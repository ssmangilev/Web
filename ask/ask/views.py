from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def testView(request,*args,**kwargs):
    return HttpResponse('OK')

