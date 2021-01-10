from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100, label='NAME')
    email = forms.EmailField(required=False, label='EMAIL')
    phone = forms.CharField(max_length=15, label='PHONE')
    subject = forms.CharField(max_length=100, label='SUBJECT')
    message = forms.CharField(widget=forms.Textarea, label='MESSAGE')