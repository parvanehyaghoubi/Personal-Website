from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='name')
    email = forms.EmailField(required=True, label='email')
    subject = forms.CharField(max_length=200, required=True, label='subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='message')
