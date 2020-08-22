from django.urls import path

from . import views
#app_name = 'user'
urlpatterns = [
    path('', views.index, name='user_index'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('siparisproduct/', views.siparisproduct, name='siparisproduct'),

    # path('addcomment/<int:id>', views.addcomment, name='addcomment'),


]