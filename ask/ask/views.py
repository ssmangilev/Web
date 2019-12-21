from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404


def testView(request,*args,**kwargs):
    try:
        return HttpResponse('OK')
    except:
        raise Http404
