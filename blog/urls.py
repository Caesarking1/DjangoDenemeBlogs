from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("addarticle/",views.addArticle,name="addarticle"),
    path("articles/",views.articles,name="articles"),
    path("detail/<int:id>",views.detail,name="detail"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("addComment/<int:id>",views.addComment,name="comments"),

]