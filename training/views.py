from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from .utils import get_zoom_join_url

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'category']

class VideoRetrieveView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

@api_view(['GET'])
def zoom_join(request, pk):
    video = Video.objects.get(pk=pk)
    url = get_zoom_join_url(video.zoom_meeting_id)
    return Response({'join_url': url})

