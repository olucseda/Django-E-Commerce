from lib2to3.fixes.fix_idioms import TYPE
from tkinter import Menu
from tokenize import Comment

from ckeditor.widgets import CKEditorWidget
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import TextInput, Select, FileInput
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from product.models import Category, Product, ContentForm, CommentForm


def index(request):
    category = Category.objects.all()
    current_user = request.user

    profile = UserProfile.objects.get(pk=current_user.id)

    context = {'category': category,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    #return HttpResponse(url)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id =id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Yorumunuz başarı ile gönderilmiştir. Teşekkür Ederiz")
            return HttpResponseRedirect(url)


    return HttpResponseRedirect(url)
@login_required(login_url='/login')  #check login
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    contents = Product.objects.filter(user_id=current_user.id)
    context = {
        'category':category,
        'comments':comments,
    }
    return render(request,'user_comments.html',context)

@login_required(login_url='/login')  #check login
def deletecomment(request,id):
    current_user = request.user
    Product.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login')
def addcontent(request):
    if request.method == 'POST': # form post edildiyse
        form = ContentForm(request.POST,request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Product()
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.price = form.cleaned_data['price']
            data.amount = form.cleaned_data['amount']
            data.detail = form.cleaned_data['detail']
            data.slug = form.cleaned_data['slug']
            data.status = 'False'
            data.save()
            messages.success(request,"Your Content Inserted successfully.")
            return HttpResponseRedirect('/user/contents')
        else:
            messages.success(request, "Content Form error :" + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        category = Category.objects.all()
        form = ContentForm()
        context = {'form':form,
               'category': category,}
        return render(request, 'user_addcontent.html', context)

@login_required(login_url='/login')
def contents(request):
    category = Category.objects.all()
    current_user = request.user
    contents = Product.objects.filter(user_id=current_user.id)
    context = {
        'category':category,
        'contents':contents,
    }
    return render(request,'user_content2.html',context)

@login_required(login_url='/login')
def contentedit(request,id):
    content = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST,request.FILES,instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Content Updated successfully.")
            return HttpResponseRedirect('/user/contents')
        else:
            messages.success(request, "Content Form error :" + str(form.errors))
            return HttpResponseRedirect('/user/contentedit'+str(id))
    else:
        category = Category.objects.all()
        form = ContentForm(instance=content)
        context = {
            'category':category,
            'form': form,
        }
        return render(request,'user_addcontent.html',context)

@login_required(login_url='/login')
def contentdelete(request,id):
    current_user = request.user
    Product.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request, 'Content deleted')
    return HttpResponseRedirect('/user/contents')