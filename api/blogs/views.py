from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets

# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
