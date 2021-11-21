from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar")
    title = models.CharField(max_length = 50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    article_image = models.FileField(blank = True,null=True,verbose_name="Fotoğraf Ekle")
    created_date = models.DateTimeField(auto_now_add = True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Yazar",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True,verbose_name="Tarih")
    def __str__(self):
        return self.comment_content

