from django.contrib import admin
from .models import NewsArticle, VideoNews

# Register your models here.
admin.site.register(NewsArticle)
admin.site.register(VideoNews)
