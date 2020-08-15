from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
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
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=225)
    keywords = models.CharField(max_length=225)
    image = models.ImageField(blank=True,upload_to='images/')
    price =models.FloatField()
    amount =models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title