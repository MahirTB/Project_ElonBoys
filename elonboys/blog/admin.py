from django.contrib import admin
from .models import Activity, BlogPost, Photo, Resource


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "is_published")
    list_filter = ("is_published", "published_at")
    search_fields = ("title", "excerpt", "content", "author")


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "location")
    list_filter = ("event_date",)
    search_fields = ("title", "description", "location")


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "link")
    list_filter = ("category",)
    search_fields = ("title", "description")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "caption")
