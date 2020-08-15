from django.contrib import admin

from home.models import Setting, ContactFormMessage

admin.site.register(Setting)
# Register your models here.
class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status']
    list_filter = ['status']

admin.site.register(ContactFormMessage, ContactFormMessageAdmin)