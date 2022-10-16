from django.urls import path, re_path
from django.views.generic import RedirectView

from base.views import MainView, JobSignupView, JobLoginView, JobLogoutView, HomeView

urlpatterns = [
    path('', MainView.as_view()),
    path('home', HomeView.as_view()),
    path('login', JobLoginView.as_view()),
    path('logout', JobLogoutView.as_view()),
    path('signup', JobSignupView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
]
