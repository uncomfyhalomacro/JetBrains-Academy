from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from .models import  Vacancy
from .forms import VacancyForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
# Create your views here.

class VacancyListView(View):
    template_name = "vacancy/vacancy_list.html"
    queryset = Vacancy.objects.all()
    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'title': "Vacancy Listings ~ HyperJob Agency", 'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class VacancyCreateView(View):
    def get(self, request):
        print(request.user.is_staff)
        if request.user.is_authenticated and request.user.is_staff:
            form = VacancyForm()
            context = dict(title="Create Resume ~ HyperJob Agency", form=form)
            return render(request, 'create_new_resume.html', context)
        else:
            raise PermissionDenied

    def post(self, request):
        if request.method == "POST":
            if request.user.is_authenticated and request.user.is_staff:
                author = request.user
                description = request.POST.get('description')
                print(author)
                print(description)
                form = Vacancy(author=author, description=description)
                form.save()
                return redirect('/home')
            else:
                raise PermissionDenied