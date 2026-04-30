from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    excerpt = models.TextField(max_length=500)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    cover_image = models.ImageField(upload_to="media/blog/images/", blank=True)
    published_at = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(max_length=500)
    event_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=140, blank=True)
    image = models.ImageField(upload_to="media/activities/images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-event_date", "-created_at"]
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title


class Resource(models.Model):
    CATEGORY_CHOICES = [
        ("notes", "Course notes"),
        ("career", "Career prep"),
        ("tools", "Developer tools"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=180)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    link = models.URLField(blank=True)
    file = models.FileField(upload_to="media/resources/files/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "-created_at"]

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="media/photos/images/")
    caption = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
