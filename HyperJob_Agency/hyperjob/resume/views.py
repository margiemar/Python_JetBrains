from django.shortcuts import render
from django.views import View
from .models import Resume
from django.http import HttpResponse
from django.contrib.auth.models import User





class ResumeListView(View):
    def get(self, request):
        resume_list = Resume.objects.all()
        return render(request, "all_resumes.html", {'resume_list': resume_list})

class NewResumeView(View):
    def post(self, request):
        #if request.user.is_authenticated:
        if not request.user.is_staff:
            desc = request.POST.get("description")
            user = User.objects.get(username=request.user.username)
            Resume.objects.create(author=user, description=desc)
            return render(request, "all_resumes.html", {'resume_list': Resume.objects.all()})
        else:
            return HttpResponse(status=403)

    def get(self, request):
        return render(request, "NewResume.html")

