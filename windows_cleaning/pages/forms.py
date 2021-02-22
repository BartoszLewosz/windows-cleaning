from django import forms

class ContactForm(forms.Form):
    # your_name = forms.CharField(max_length=100, label='NAME', error_messages={'required': 'Please enter your name'})
    email = forms.EmailField(label='EMAIL', error_messages={'required': 'Please enter your email'})
    # phone = forms.CharField(max_length=15, required=False, label='PHONE', error_messages={'required': 'Please enter your phone number'})
    subject = forms.CharField(required=False, max_length=100, label='SUBJECT')
    message = forms.CharField(widget=forms.Textarea, label='MESSAGE', error_messages={'required': 'Please enter some details'})

class ContactFormTwo(forms.Form):
    name = forms.CharField(max_length=80)
    msg = forms.CharField(widget=forms.Textarea)
    e_mail = forms.EmailField()