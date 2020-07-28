"""Django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import include
from User.views import IndexView
from User import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('home/', views.home),
                  path('admin/', admin.site.urls),
                  path('captcha/', include('captcha.urls')),
                  path('refresh_captcha/', views.refresh_captcha),
                  path('', IndexView.as_view()),
                  path('Market/', include('Market.urls')),
                  path('Problem/', include('Problem.urls')),
                  path('User/', include('User.urls')),
                  path('Project/', include('Project.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
