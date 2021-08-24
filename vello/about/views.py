from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from vello.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .models import About_main,About_one,About_partners

def about(request):
    about_main = About_main.objects
    about_one = About_one.objects
    about_partners = About_partners.objects
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return render(request, "about/about.html", {'form': form,'about_main':about_main,'about_one':about_one,' about_partners': about_partners})
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "about/about.html", {'form': form,'about_main':about_main,'about_one':about_one,'about_partners': about_partners})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')


