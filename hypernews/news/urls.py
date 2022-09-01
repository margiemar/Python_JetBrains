from django.urls import path, re_path
from django.conf.urls.static import static
from hypernews import settings
from news.views import WelcomeView, InfoView, AllNewsView, CreateNewView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/news/')),
    path('news/<int:link_identifier>/', InfoView.as_view()),
    path('news/create/', CreateNewView.as_view()),
    re_path('news/', AllNewsView.as_view()),
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
