from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, default="title")
    picture = models.URLField(default="https://picsum.photos/id/12/300/500")
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    last_updated = models.DateField(auto_now=True)
    author = models.CharField(max_length=100, default="Jeff Salisbury")
    # "tags" = [
    #     {"id" = "0", "name" = "live"},
    #     {"id" = "1", "name" = "Dragons"},
    #     {"id" = "2", "name" = "Robots"}
    # ]

    def __str__(self):
        return self.title
