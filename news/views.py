from rest_framework import generics
from django.core.cache import cache
from .models import NewsArticle, VideoNews
from .serializers import NewsArticleSerializer, VideoNewsSerializer

# Create your views here.

class LatestNewsArticleList(generics.ListAPIView):
    serializer_class = NewsArticleSerializer
    
    def get_queryset(self):
        # Attempt to fetch cached news articles
        cached_articles = cache.get("latest_news_articles")
        if cached_articles is None:
            # Query db for latest 8 articles
            cached_articles = list(NewsArticle.objects.all()[:8])
            # Cache the queryset for 5 mins (300s)
            cache.set("latest_news_articles", cached_articles, 300)
        return cached_articles


class LatestVideoNews(generics.RetrieveAPIView):
    serializer_class = VideoNewsSerializer

    def get_object(self):
        # Attempt to get cached news video
        cached_video = cache.get("latest_video_news")
        if cached_video is None:
            # Query db to get latest video
            cached_video = VideoNews.objects.first()
            # Cache retrieved video
            cache.set("latest_video_news", cached_video, 300)
        return cached_video
