from django.contrib import admin
from .models import Blog, Tag
from django.utils.html import format_html


class BlogAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    # list_display = ['title', 'created_at', 'picture']

    def image_tag(self, obj):
        return format_html('<img style="height: 25%"  src="{}" />'.format(obj.picture))

    image_tag.short_description = 'Image'

    list_display = ['title', 'created_at', 'image_tag']
    readonly_fields = ['views', 'image_tag', 'created_at', 'last_updated']

    fieldsets = (
        (None, {
            "fields": (
                'title',
                'body',
                'picture',
                'image_tag',
                'tags',
            ),
        }),
        ('Meta Data', {
            'classes': ('collapse',),
            'fields': (
                'views',
                'author',
                'created_at',
                'last_updated'
            )
        })
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
