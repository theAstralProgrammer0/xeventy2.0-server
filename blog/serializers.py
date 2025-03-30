"""
This serializer converts the <Article> model into a JSON format that the front
end can consume
"""

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'image_src', 'blog_url', 'created_at']

