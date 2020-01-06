from qa.models import Session
from django.utils import timezone
import datetime
class CheckSessionMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        try:
            sessid=request.COOKIES.get('sessid')
            session=Session.objects.get(
            key=sessid,
            expires__gt=timezone.datetime.now()
            )
            request.session=session
            request.user=session.user_id
        except Session.DoesNotExist:
            request.session=None
            request.user=None
        response = self.get_response(request)
        return response         