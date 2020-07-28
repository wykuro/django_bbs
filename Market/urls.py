from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from Django_bbs import settings
from . import views

urlpatterns = [
    path('', views.market),
    re_path('detail/(\d+)/', views.item),
    re_path('delete/(\d+)/', views.delete),
    path('search/', views.search),
    path('user_market/', views.user_market),
    path('market_sub/', views.market_sub),
    path('category/1', views.category1),
    path('category/2', views.category2),
    path('category/3', views.category3),
    path('category/4', views.category4),
    path('category/5', views.category5),
    path('category/6', views.category6),
]
