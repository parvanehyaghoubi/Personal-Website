from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .form import ContactForm


def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            email = cd['email']
            subject = cd['subject']
            message = cd['message']

            print(f"name: {name}")
            print(f"email: {email}")
            print(f"subject: {subject}")
            print(f"message: {message}")

            msg = "name{0}\nemail:{1}\nmessage:\n{2}".format(name, email, message)
            send_mail(subject, msg, 'parvanehyaghoubi98@gmail.com', ['parvanehyaghoubi98@gmail.com'], fail_silently=False)
            sent = True
    else:
        form = ContactForm()
    return render(request, template_name='index.html', context={'form': form, 'sent': sent})
