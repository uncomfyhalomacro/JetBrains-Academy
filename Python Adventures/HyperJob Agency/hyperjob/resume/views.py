from django.shortcuts import render, redirect
from django.views import View
from .models import  Resume
from .forms import ResumeForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

# Create your views here.

class ResumeListView(View):
    template_name = "resume/resume_list.html"
    queryset = Resume.objects.all()
    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'title': "Resume Listings ~ HyperJob Agency", 'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class ResumeCreateView(View):
    def get(self, request):
        print(request.user.is_staff)
        if request.user.is_authenticated or request.user.is_staff:
            form = ResumeForm()
            context=dict(title="Create Resume ~ HyperJob Agency", form=form)
            return render(request, 'create_new_resume.html', context)
        else:
            raise PermissionDenied

    def post(self, request):
        if request.method == "POST":
            author = request.user
            description = request.POST.get('description')
            print(author)
            print(description)
            form = Resume(author=author, description=description)
            form.save()
            return redirect('/home', permanent=False, kwargs={'author': author, 'description': description})
