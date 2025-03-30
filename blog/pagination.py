"""
By returning a JSON structure that includes 'links' for the next and prev
pages, we are following a HATEOAS approach. This makes this API
seld-descriptive in terms of navigation.
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class HATEOASPagination(PageNumberPagination):
    page_size = 10      # numner of articles per page

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'prev': self.get_prev_link(),
            },
            'count': self.page.paginator.count,
            'results': data
        })
