from django.shortcuts import get_object_or_404, redirect, render,reverse

from blog.forms import ArticleForm
from .models import Article, Comment
from blog import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"index.html",{"articles":articles})
    articles = Article.objects.all()
    articles = Article.objects.all()
    return render(request,"index.html",{"articles":articles})




    return render(request,"index.html",context)
@login_required(login_url="register")
def articles(request):
    article = Article.objects.filter(author = request.user)
    context = {
        "article":article
    }
    return render(request,"articles.html",context)



def about(request):
    return render(request,"about.html")


@login_required(login_url="login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Kayıt Edildi..")
        return redirect("index")
    return render(request,"addarticle.html",{"form":form})


def detail(request,id):
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})



def update(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect("articles")
    return render(request,"update.html",{"form":form})

    
def delete(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("articles")


def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content = comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("detail",kwargs = {"id":id}))