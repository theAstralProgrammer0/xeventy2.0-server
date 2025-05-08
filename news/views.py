from rest_framework import generics
from rest_framework.response import Response
from django.core.cache import cache
from .models import NewsArticle, VideoNews
from .serializers import NewsArticleSerializer, VideoNewsSerializer

# Create your views here.

class LatestNewsArticleList(generics.ListAPIView):
    """
    Latest 8 news articles, cached, pagination off.
    """
    serializer_class = NewsArticleSerializer
    
    # DISABLE PAGINATION
    pagination_class = None

    # REDIS CACHING
    def get_queryset(self):
        """
        Attempt to fetch cached news articles
        """
        cache_key = "latest_news_articles"
        cached_articles = cache.get(cache_key)
        if cached_articles is None:
            # Query db for latest 8 articles
            cached_articles = list(NewsArticle.objects.all().order_by('-published_at')[:8])
            # Cache the queryset for 30mins
            cache.set(cache_key, cached_articles, 1800) 
        return cached_articles


class LatestVideoNews(generics.RetrieveAPIView):
    """
    Latest video news, cached, pagination off.
    """
    serializer_class = VideoNewsSerializer

    # DISABLE PAGINATION
    pagination_class = None
    
    # REDIS CACHING
    def get_object(self):
        # Attempt to get cached news video
        cache_key = "latest_video_news"
        cached_video = cache.get(cache_key)
        if cached_video is None:
            # Query db to get latest video
            cached_video = VideoNews.objects.first()
            # Cache retrieved video for 30mins
            cache.set("latest_video_news", cached_video, 1800)
        return cached_video
