from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . models import Page

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'permalink': pg.permalink,
        'content': pg.body_text,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False - uncomment to see error page and check local vars
    return render(request, 'pages/page.html', context)
