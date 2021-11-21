from django.contrib import admin
from .models import Article,Comment

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["author","title"]
    class Meta:
        model = Article



admin.site.register(Comment)




