from django.urls import path

from . import views
#app_name = 'user'
urlpatterns = [
    path('', views.index, name='user_index'),
    # path('addcomment/<int:id>', views.addcomment, name='addcomment'),


]