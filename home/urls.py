from xml.etree.ElementInclude import include

from django.urls import path

from . import views, admin
from home import views
urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('referanslarımız/', views.referanslarımız, name='referanslarımız'),
    path('turlarımız/', views.turlarımız, name='turlarımız'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),


    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
]
