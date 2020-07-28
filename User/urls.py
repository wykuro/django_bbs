from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from Django_bbs import settings
from User.views import register, create, update
from . import views

urlpatterns = [
    path('', views.user),
    path('logout/', views.log_out),
    path('register/', register.as_view()),
    path('update/', update.as_view()),
    path('create/', create.as_view())
]
