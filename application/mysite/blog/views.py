from django.http import HttpResponse
from django.template import Context, Template
from django.template.loader import get_template


def current_datetime(request) :
    t = get_template('base.html')
    c = Context()
    html = t.render(c)
    return HttpResponse(html)
