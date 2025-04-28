import requests
from django.conf import settings

def get_zoom_join_url(meeting_id):
    return f"https://zoom.us/j/{meeting_id}"

