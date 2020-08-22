from lib2to3.fixes.fix_idioms import TYPE
from tkinter import Menu
from tokenize import Comment

from ckeditor.widgets import CKEditorWidget
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from product.models import Category, Product, ContentForm, CommentForm
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user

    profile = UserProfile.objects.get(pk=current_user.id)

    context = {'category': category,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)

@login_required(login_url='/login')
def user_update(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user) #request user is user session data

        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your account has been updated!')
            return  redirect('/user')

    else:
        category= Category.objects.all()
        user_form=UserUpdateForm(instance=request.user)# user form user ile ilişki kuracak
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)

        context={
            'category':category,
            'user_form':user_form,
            'profile_form':profile_form,
        }
        return  render(request,'user_update.html',context)

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was succesfully updated!')
            return  redirect('change_password')
        else:
            messages.error(request,'Please correct the error below.<br>'+str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category=Category.objects.all()
        form=PasswordChangeForm(request.user)
        return render(request,'change_password.html',{
            'form':form,'category':category
        })

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
        'comments':comments,'contents':contents,
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