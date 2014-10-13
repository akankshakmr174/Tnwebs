from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
def home(request):
    # View code here...
    t = loader.get_template('tnhome.html')
    c = RequestContext(request, {'foo': 'bar'})
    return HttpResponse(t.render(c))


def particle(request):
    # View code here...
        l = loader.get_template('index.html')
        m = RequestContext(request, {'foo': 'bar'})
        return HttpResponse(l.render(m))

