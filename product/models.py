from lib2to3.fixes.fix_idioms import TYPE
from tkinter import Menu
from tokenize import Comment
from urllib import request

from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Select, FileInput
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel



class Category(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=225)
    keywords = models.CharField(max_length=225)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS,)
    detail = RichTextUploadingField()
    slug = models.SlugField()
    parent = TreeForeignKey('self',blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=225)
    keywords = models.CharField(max_length=225)
    image = models.ImageField(blank=True,upload_to='images/')
    price =models.FloatField()
    amount =models.IntegerField()
    detail = RichTextUploadingField(blank=True)
    slug = models.SlugField(blank=True, max_length=150)
    status = models.CharField(max_length=10, choices=STATUS,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'slug': self.slug})

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']

class ContentForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'keywords', 'description','image','price','amount','detail', 'slug']
        widgets = {
            'category': Select(attrs={'class': 'input', 'placeholder': 'category'}),
            'title'     :TextInput(attrs={'class': 'input','placeholder':'title'}),
            'slug'     : TextInput(attrs={'class': 'input', 'placeholder': 'slug'}),
            'keywords'        : TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description'            : TextInput(attrs={'class': 'input', 'placeholder': 'descrition'}),
            'price': TextInput(attrs={'class': 'input', 'placeholder': 'price'}),
            'amount': TextInput(attrs={'class': 'input', 'placeholder': 'amount'}),
            'image'        :  FileInput(attrs={'class': 'input', 'placeholder': 'imge'}),
            'detail'        :CKEditorWidget()
        }

