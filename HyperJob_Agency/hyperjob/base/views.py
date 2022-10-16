from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView


class MainView(View):
    def get(self, request):
        return render(request, "mainpage.html")

class JobSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

class JobLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

class JobLogoutView(LogoutView):
    redirect_authenticated_user = True

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
