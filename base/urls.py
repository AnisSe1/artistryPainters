from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # path("login/", views.login_page, name="login"),
    path("contact/", views.contact, name="contact"),
]
