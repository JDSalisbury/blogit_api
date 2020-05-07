from .models import Blog, Tag
from .serializers import BlogSerializer, TagSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from familiar.familiar import get_game_version, dice_roll
# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'data': data
        })


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = BlogPagination

    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
        "tags__name",
    ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        serializer.data[0]['value'] = get_game_version()
        serializer.data[0]['dice_roll'] = dice_roll(2, 6, 0)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = BlogSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)
