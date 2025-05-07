from django.shortcuts import render, redirect
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        name_ = request.POST['name']
        email_ = request.POST['email']
        subject_ = request.POST['subject']
        message_ = request.POST['message']
        msg = "name:\n{0}\nemail:\n{1}\nmessage:\n{2}".format(name_, email_, message_)

        send_mail(
            subject_,
            msg,
            'parvanehyaghoubi98@gmail.com',
            ['parvanehyaghoubi98@gmail.com'],
            fail_silently=False,
        )

        return render(request, template_name='confirmation.html', context={'name_': name_})
    else:
        return render(request, template_name='index.html')
