from django.urls import path

from . import views
#app_name = 'user'
urlpatterns = [
    path('', views.index, name='user_index'),
    path('comments/', views.comments, name='comments'),
    path('addcontent/', views.addcontent, name='user_addcontent'),
    path('contents/', views.contents, name='user_content'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('contentdelete/<int:id>', views.contentdelete, name='contentdelete'),
    path('comments/', views.comments, name='user_comments'),

]
