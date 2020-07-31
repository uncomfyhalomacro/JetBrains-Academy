"""hyperjob URL Configuration

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
from django.urls import path
from pages.views import MainView, LoginView, SignUpView, HomeView
from resume.views import ResumeListView, ResumeCreateView
from vacancy.views import VacancyListView, VacancyCreateView
from django.views.generic import RedirectView

urlpatterns = [
    path("home", HomeView.as_view(), name="home"),
    path('home/', RedirectView.as_view(url="/home")),
    path('vacancy/new', VacancyCreateView.as_view(), name="create_vacancy"),
    path('resume/new', ResumeCreateView.as_view(), name="create_resume"),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('signup', SignUpView.as_view(), name="signup_site"),
    path('login',  LoginView.as_view(), name="login_site"),
    path('vacancies', VacancyListView.as_view(), name="vacancy_list"),
    path('resumes/', ResumeListView.as_view(), name="resume_list"  ),
    path('', MainView.as_view(), name="main"),
    path('admin/', admin.site.urls),
]
