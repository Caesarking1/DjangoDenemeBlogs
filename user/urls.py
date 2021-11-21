from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name="logout"),

]