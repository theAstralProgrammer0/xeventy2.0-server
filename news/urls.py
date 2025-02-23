from django.urls import path
from .views import LatestNewsArticleList, LatestVideoNews


urlpatterns = [
    path('news-articles/', LatestNewsArticleList.as_view(), name='news-articles'),
    path('video-news/', LatestVideoNews.as_view(), name='video-news'),
]
