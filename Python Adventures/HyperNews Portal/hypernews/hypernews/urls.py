"""hypernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include

from news.views import main_view, future_page, news_page, create_page

urlpatterns = [
    #path('news/create/', about_page, name="about page"),
    path('', future_page, name="future page"),
    #path('news/coming_soon/', future_page),
    path('not-existing-link-by-default/', main_view),
    path('news/<int:link>/', news_page, name="news pages"),
    #path('news/2/', news_page, name="The raise of Jupyter"),
    #path('news/3/', news_page),
    path('news/create/', create_page),
    re_path('news/', main_view, name="main page"),
    path('admin/', admin.site.urls),
]
