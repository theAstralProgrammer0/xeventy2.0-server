from django.db import models
from django.utils import timezone

# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_timeline(self):
        now = timezone.now()
        time_difference = now - self.published_at

        if time_difference < timezone.timedelta(minutes=1):
            return "Just Now"
        elif time_difference < timezone.timedelta(hours=1):
            minutes = time_difference.seconds // 60
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        elif time_difference < timezone.timedelta(days=1):
            hours = time_difference.seconds // 3600
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif time_difference < timezone.timedelta(days=7):
            days = time_difference.days
            return f"{days} day{'s' if days > 1 else ''} ago"
        else:
            return self.published_at.strftime("%B %d, %Y") # "February 21, 2025"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Calling the original save method


class VideoNews(models.Model):
    title = models.CharField(max_length=255)
    content_provider = models.CharField(max_length=255)
    youtube_url = models.URLField(help_text="YouTube video link")
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
