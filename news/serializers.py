from rest_framework import serializers
from .models import NewsArticle, VideoNews
from django.utils import timezone


class NewsArticleSerializer(serializers.ModelSerializer):
    # Compute a timeline val. using published_at frm d get_timeline meth
    # in models
    timeline = serializers.SerializerMethodField()

    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'author', 'published_at', 'timeline', 'content']

    def get_timeline(self, obj):
        # Instantiated obj calls d method here
        return obj.get_timeline()


class VideoNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoNews
        fields = ['id', 'title', 'content_provider', 'youtube_url', 'published_at']

