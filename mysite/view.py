from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return HttpResponse('Hello World')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><title></title><body>It is now {}.</body></html>".format(now)
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(offset)
    html = "<html><title></title><body>It is now {}.</body></html>".format(dt)
    return HttpResponse(html)