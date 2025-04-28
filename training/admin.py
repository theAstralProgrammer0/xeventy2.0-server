from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_live', 'scheduled_time')
    list_filter = ('category', 'is_live')
    search_fields = ('title', 'description')
    ordering = ('-scheduled_time',)

