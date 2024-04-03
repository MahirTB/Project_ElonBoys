# Generated by Django 5.0.3 on 2024-04-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image1", models.ImageField(upload_to="media/member/images/")),
                ("image2", models.ImageField(upload_to="media/member/images/")),
                ("designation", models.CharField(max_length=100)),
                ("github_link", models.URLField(blank=True)),
                ("linkedin_link", models.URLField(blank=True)),
                ("instagram_link", models.URLField(blank=True)),
                ("resume", models.FileField(blank=True, upload_to="members/resumes/")),
            ],
        ),
    ]