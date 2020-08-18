
from django.urls import path

from . import views
from home import views
urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('referanslarımız/', views.referanslarımız, name='referanslarımız'),
    path('turlarımız/', views.turlarımız, name='turlarımız'),

    # ex: /home/5/
    #path('<int:question_id>/', views.detail, name='detail'),

]