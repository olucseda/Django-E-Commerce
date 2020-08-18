from pyexpat.errors import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
import home
from home.models import Setting, ContactFormMessage, ContactFormu
from product.models import Category, Product


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    popularplaces = Product.objects.all()[:3]



    context = {'setting': setting,
               'page': home,
               'category': category,
               'popularplaces': popularplaces,
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting, }
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'iletisim.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context={'setting':setting,'form':form}
    return render(request,'iletisim.html',context)

def referanslarımız(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting, }
    return render(request, 'referanslarımız.html', context)

def turlarımız(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting, }
    return render(request, 'turlarımız.html', context)

