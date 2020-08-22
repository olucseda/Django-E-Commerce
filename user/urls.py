from django.urls import path

from . import views
#app_name = 'user'
urlpatterns = [
    path('', views.index, name='user_index'),
    path('update/',views.user_update,name='user_update'),
    path('password/',views.change_password,name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('addcontent/', views.addcontent, name='user_addcontent'),
    path('contents/', views.contents, name='user_content'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('contentdelete/<int:id>', views.contentdelete, name='contentdelete'),


]
