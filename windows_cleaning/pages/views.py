from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.core.mail.message import EmailMessage
from windows_cleaning.settings import DEFAULT_FROM_EMAIL

from . models import Page
from .forms import ContactForm

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
    # assert False
    # - uncomment to see error page and check local vars
    return render(request, 'pages/page.html', context)

def privacy(request):
    return render(request, 'pages/privacy.html')
    
def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message_body = cd['message']
            client_email = cd['email']
            try:
                contact_form_email = EmailMessage(
                    subject=subject,
                    body = message_body,
                    to=[DEFAULT_FROM_EMAIL],
                    reply_to=[client_email]
                )
                contact_form_email.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Bad header')
            
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {
        'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})