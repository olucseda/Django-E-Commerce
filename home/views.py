from email.mime import image
from pyexpat.errors import messages

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
import home
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormMessage, ContactFormu, Setting, UserProfile
from product.models import Category, Product, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    images = Images.objects.get(pk=9)
    dayproducts = Product.objects.all()[:3]
    lastproducts = Product.objects.all().order_by('-id')[:6]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'setting': setting,
               'category': category,
               'images': images,
               'page': 'home',
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting':setting, 'category': category }
    return render(request, 'hakkimizda.html', context)




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
    category = Category.objects.all()
    context={'setting':setting,'form':form, 'category':category}
    return render(request,'iletisim.html',context)

def referanslarımız(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting':setting, 'category': category}
    return render(request, 'referanslarımız.html', context)
def category_products(request,id,slug,image):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    setting = Setting.objects.get(pk=1)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               'setting': setting,
               'categorydata': categorydata,
               'image': image,}
    return render(request, 'products.html', context)

def product_detail(request,id,slug,image):
    category = Category.objects.all()
    context = {#'products': products,
               'category': category,
                'image': image,}
    return render(request, 'product_detail.html',context)
def turlarımız(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting':setting,'category':category }

    return render(request, 'turlarımız.html', context)

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:

            return HttpResponseRedirect('/login')


    category = Category.objects.all()
    context= {'category': category,
              'image': image,}
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    context= {'category': category,
              'form': form,
             }
    return render(request, 'signup.html', context)