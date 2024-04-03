from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='media/member/images/')
    image2 = models.ImageField(upload_to='media/member/images/')
    bio = models.CharField(max_length=100)
    description =models.TextField(max_length=500, blank=True)
    facebook_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    resume = models.FileField(upload_to='media/member/resumes/', blank=True)

    def __str__(self):
        return self.name
