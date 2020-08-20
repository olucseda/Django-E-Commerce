from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
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

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'

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

    def cating_tag(self):
        return mark_safe((Category.status))

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'