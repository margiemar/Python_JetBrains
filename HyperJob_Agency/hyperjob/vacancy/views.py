from django.shortcuts import render
from django.views import View
from .models import Vacancy
from django.http import HttpResponse
from django.contrib.auth.models import User





class VacanciesListView(View):
    def get(self, request):
        vacancy_list = Vacancy.objects.all()
        return render(request, "all_vacancies.html", {'vacancy_list': vacancy_list})

class NewVacancyView(View):
    def post(self, request):
        #if request.user.is_authenticated and request.user.is_staff:
        if request.user.is_staff:
            desc = request.POST.get("description")
            user = User.objects.get(username=request.user.username)
            Vacancy.objects.create(author=user, description=desc)
            return render(request, "all_vacancies.html", {'vacancy_list': Vacancy.objects.all()})
        else:
            return HttpResponse(status=403)

    def get(self, request):
        return render(request, "NewVacancy.html")
