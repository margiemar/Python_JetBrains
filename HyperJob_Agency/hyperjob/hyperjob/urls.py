from django.urls import path, include
from vacancy.urls import vacancy_patterns
from resume.urls import resume_patterns
from resume.views import NewResumeView
from vacancy.views import NewVacancyView

urlpatterns = [
    path('', include('base.urls')),
    path("resumes", include(resume_patterns)),
    path("vacancies", include(vacancy_patterns)),
    path("resume/new", NewResumeView.as_view()),
    path("vacancy/new", NewVacancyView.as_view())
]
