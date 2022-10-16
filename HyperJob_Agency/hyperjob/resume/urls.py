from django.urls import path, re_path
from .views import ResumeListView, NewResumeView

resume_patterns = [
    path('', ResumeListView.as_view()),
]

