import django.urls

from . import views

urlpatterns = [
    # ex: /home/
    django.urls.path('', views.index, name='index'),


]
