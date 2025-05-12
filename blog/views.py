"""
This view uses DRF's generic <ListAPIView> to serve articles. By overriding
the <list()> method, it first checks if a cached response exists (using a key
that depends on the requested page) and returns that if available. if not, it
computes the respondse and cached it. This reduces database queries thanks to
redis caching 
"""

from rest_framework import generics
from rest_framework.response import Response
from django.core.cache import cache
from .models import Article
from .serializers import ArticleSerializer
from .pagination import HATEOASPagination

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer

    # ENABLE PAGINATION
    pagination_class = HATEOASPagination

    # OVERRIDE DEFAULT PAGE SIZE
    def get_paginate_by(self, queryset):
        """
        Get 'page_size' from request
        If None, use 10 as default page size for pagination
        """
        return self.request.GET.get('page_size', 4) 

    # REDIS CACHING AND RETURN
    def list(self, request, *args, **kwargs):
        """
        Use the 'page' query parameter as part of the cache key.
        If None, use 1
        """
        page = request.query_params.get('page', 1)
        cache_key = f'articles_page_{page}'
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response)

        response = super().list(request, *args, **kwargs)
        # Cache the paginated response for 5 minutes (300 seconds)
        cache.set(cache_key, response.data, 1800)
        return response

