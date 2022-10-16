from django.urls import path, re_path
from .views import VacanciesListView, NewVacancyView

vacancy_patterns = [
    path('', VacanciesListView.as_view()),
]
