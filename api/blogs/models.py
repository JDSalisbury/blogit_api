from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    icon = models.URLField(max_length=200)

    def __str__(self):
        return self.name


def get_default_url():
    # tag = Tag.objects.get(pk=0)
    tag = get_object_or_404(Tag, pk=1)

    return tag.icon


def get_max_amount():
    return 4


class Blog(models.Model):

    title = models.CharField(max_length=255, default="title")
    picture = models.URLField(default=get_default_url)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    last_updated = models.DateField(auto_now=True)
    author = models.CharField(max_length=100, default="Jeff Salisbury")
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
