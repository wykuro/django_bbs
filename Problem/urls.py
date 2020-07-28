from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from Django_bbs import settings
from . import views

urlpatterns = [
    path('', views.problem),
    re_path('detail/(\d+)/', views.item, name='detail_pm'),
    re_path('delete/(\d+)/', views.delete),
    path('comment_sub/', views.comment_sub),
    path('user_problem/', views.user_problem),
    path('problem_sub/', views.problem_sub),
]
