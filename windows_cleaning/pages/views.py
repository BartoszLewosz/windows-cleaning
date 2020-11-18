from django.shortcuts import render
from django.http import HttpResponse

from . models import Page

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.body_text,
        'last_updated': pg.update_date,
    }
    # assert False
    return render(request, 'pages/page.html', context)
