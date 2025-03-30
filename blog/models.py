"""
This model stores the title, description, image_src, blog_url, and 
created_at field for ordering articles
"""

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_src = models.URLField()
    blog_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

