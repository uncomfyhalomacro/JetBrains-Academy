from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from resume.forms import ResumeForm, Resume
# Create your views here.
class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        profile_context = {
            'title': "Home ~ HyperJob Agency",
            'form': form
        }
        return render(request, 'home.html', profile_context)

    def post(self, request):
        if request.user.is_authenticated or request.user.is_staff:
            if request.method == "POST":
                author = request.user
                description = request.POST.get('description')
                print(description)
                form = Resume(author=author, description=description)
                form.save()
                return redirect('/', permanent=False, kwargs={'author': author, 'description': description})


class MainView(View):
    def get(self, request):
        page_context = {
            'title': "Welcome to HyperJob!",
            'links': [
                {'title': 'Login', 'link_to': "login"},
                {'title': 'Sign Up', 'link_to': "signup"},
                {'title': 'Vacancies', 'link_to': "vacancies"},
                {'title': 'Resumes', 'link_to': "resumes"},
                {'title': 'Home', 'link_to': "home"}, ]
        }
        return render(request, 'main.html', context=page_context)


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        context = {
            'title': "Sign Up ~ HyperJob Agency",
            'form': form
        }
        return render(request, 'signup.html', context)

    def post(self, request):
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('/login')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'title': "Login ~ HyperJob Agency",
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            print(request.user)
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
