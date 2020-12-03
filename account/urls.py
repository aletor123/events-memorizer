from django.urls import path

from . import views
from django.contrib.auth import views as django_auth_views

app_name = 'account'

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", django_auth_views.LogoutView.as_view(), name="logout"),
    path("", views.start_page, name="home"),
]
