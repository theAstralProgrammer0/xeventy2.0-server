from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import Video
from .serializers import VideoSerializer
from .utils import get_zoom_join_url

class VideoListCreateView(generics.ListCreateAPIView):
    """
    List & create videos with Redis caching and no pagination.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'category']

    # DISABLE PAGINATION
    pagination_class = None

    # REDIS CACHING
    def list(self, request, *args, **kwargs):
        """
        Add Redis caching:
        - Cache key per search+page (here just search param)
        - Return cached if present, else fetch, cache, return
        """
        search = request.query_params.get('search', '')
        cache_key = f'videos_list_search_{search or "all"}'
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, 1800) # cache for 30 mins
        return response



class VideoRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve a single video. Also cached.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    # DISABLE PAGINATION 
    pagination_class = None

    # REDIS CACHING
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cache_key = f'video_detail_{pk}'
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, 1800) # cache for 30 m
        return response


@api_view(['GET'])
def zoom_join(request, pk):
    video = Video.objects.get(pk=pk)
    # No pagination here; just a simple endpoint
    url = get_zoom_join_url(video.zoom_meeting_id)
    return Response({'join_url': url})

