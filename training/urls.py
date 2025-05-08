from django.urls import path
from .views import VideoListCreateView, VideoRetrieveView, zoom_join

urlpatterns = [
    path('videos/', VideoListCreateView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoRetrieveView.as_view(), name='video-detail'),
    path('videos/<int:pk>/zoom/', zoom_join, name='video-zoom-join'),
]

