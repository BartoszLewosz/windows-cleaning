from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, get_connection, BadHeaderError
from django.core.mail.message import EmailMessage
from windows_cleaning.settings import DEFAULT_FROM_EMAIL

from . models import Page
from .forms import ContactForm, ContactFormTwo

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
            email = form.cleaned_data["email"]
            # insert variables that respond the ContactForm
            send_mail(
                'Subject here', # place the variables from above
                'Here is the message',
                # from_email=DEFAULT_FROM_EMAIL
                DEFAULT_FROM_EMAIL,
                ['bartosz.lewosz@gmail.com'],
                fail_silently=False,
            )
            #cd = form.cleaned_data
            # assert False
            # con = get_connection('django.core.mail.backends.console.EmailBackend')
            
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {
        'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})

def contact_two(request):
    form = ContactFormTwo()
    if request.method == "POST":
        form = ContactFormTwo(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["name"]
            message = form.cleaned_data["msg"]
            recipient = ['code.levee@gmail.com']
            client_email = form.cleaned_data['e_mail']
            try:
                email_test = EmailMessage(
                    subject,
                    message,
                    recipient,
                    to=[DEFAULT_FROM_EMAIL],
                    # set DFAULT_FROM_EMAIL for validated sender in sendgrid when domain is ready
                    reply_to=[client_email],
                )
                email_test.send(fail_silently=False)
            # try:
            #     send_mail(
            #         subject,
            #         message,
            #         ['code.levee@gmail.com'],
            #         recipient, fail_silently=False
            #     )
            except BadHeaderError:
                return HttpResponse('Bad header')

            return HttpResponse('success..!!')

    return render(request, 'pages/contact_two.html', {'form': form})