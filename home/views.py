from pyexpat.errors import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from home.models import Setting, ContactFormMessage
from product.models import Category


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting, 'page':'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting, }
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    if request.method == 'POST':  # check post
        form = ContactFormMessage(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get(pk=1)
    form = ContactFormMessage()
    context = {'setting':setting,  'form':form}
    return render(request, 'iletisim.html', context)