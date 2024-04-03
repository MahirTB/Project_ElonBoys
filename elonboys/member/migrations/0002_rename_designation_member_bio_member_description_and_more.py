# Generated by Django 5.0.3 on 2024-04-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member",
            old_name="designation",
            new_name="bio",
        ),
        migrations.AddField(
            model_name="member",
            name="description",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="member",
            name="facebook_link",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="resume",
            field=models.FileField(blank=True, upload_to="media/member/resumes/"),
        ),
    ]
