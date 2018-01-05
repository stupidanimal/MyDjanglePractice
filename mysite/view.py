from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
import datetime

def hello(request):
    return HttpResponse('Hello World')

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date':now})
    return HttpResponse(html)

def current_datetime2(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(offset)
    html = "<html><title></title><body>It is now {}.</body></html>".format(dt)
    return HttpResponse(html)

def testPartialView(request):   #测试一下部分页，就像.net mvc里面的 PartialView
    return render_to_response('index.html',None)