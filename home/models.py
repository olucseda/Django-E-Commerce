from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=225)
    keywords = models.CharField(max_length=225)
    company = models.CharField(max_length=30)
    adress = models.CharField(blank=True, max_length=30)
    phone = models.CharField(blank=True, max_length=30)
    fax = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=30)
    smtpserver = models.CharField(max_length=30)
    smtpemail = models.CharField(max_length=30)
    smtppassword = models.CharField(max_length=30)
    smtpport = models.CharField(max_length=30)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=30)
    instagram = models.CharField(blank=True, max_length=30)
    twitter = models.CharField(blank=True, max_length=30)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title
# Create your models here.


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed','Closed'),
    )

    name = models.CharField(blank=True,max_length=20)
    email = models.CharField(blank=True,max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True,max_length=255)
    status = models.CharField(max_length=10, choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    note = models.CharField(blank=True,max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields =['name','email','subject','message']
        widgets = {
            'name':TextInput(attrs={'class': 'field_custom','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'field_custom', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'field_custom', 'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'class': 'field_custom', 'placeholder': 'Your Message','rows':'10'}),
        }


