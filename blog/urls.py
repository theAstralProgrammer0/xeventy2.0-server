"""
This file created an endpoint (e.g. /api/blog/articles/) that my front end can
call to fetch blog data
"""

from django.urls import path
from .views import ArticleListView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
]

