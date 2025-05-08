from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_live = models.BooleanField(default=False)
    category = models.CharField(max_length=25, choices=[('training', 'Live Training'), ('event', 'Live Event'), ('saved', 'Saved')])
    youtube_url = models.URLField(blank=True, null=True)
    zoom_meeting_id = models.CharField(max_length=255, blank=True, null=True)
    zoom_join_url = models.URLField(blank=True, null=True)
    scheduled_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

