import platform
import re
import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from blog.models import Activity, BlogPost, Photo, Resource
from .models import Member
# Create your views here.


class HomeView(View):
    def get(self, request):
        members = Member.objects.all()
        return render(request, "index.html", {"members": members})


class MemberView(View):
    def get(self, request):
        members = Member.objects.all()
        return render(request, "member.html", {"members": members})


class BlogView(View):
    def get(self, request):
        posts = BlogPost.objects.filter(is_published=True)
        return render(request, "blogs.html", {"posts": posts})


class ActivitiesView(View):
    def get(self, request):
        activities = Activity.objects.all()
        return render(request, "activities.html", {"activities": activities})


class ResourcesView(View):
    def get(self, request):
        resources = Resource.objects.all()
        return render(request, "resources.html", {"resources": resources})


class PhotosView(View):
    def get(self, request):
        photos = Photo.objects.all()
        members = Member.objects.all()
        return render(request, "photos.html", {"photos": photos, "members": members})


class ToolsView(View):
    def get(self, request):
        return render(request, "tools.html")


class PingToolView(View):
    target_pattern = re.compile(r"^[a-zA-Z0-9.-]{1,253}$")

    def get(self, request):
        target = request.GET.get("target", "").strip()

        if not target or not self.target_pattern.match(target) or ".." in target:
            return JsonResponse(
                {"error": "Enter a valid IP address or hostname."},
                status=400,
            )

        is_windows = platform.system().lower() == "windows"
        command = ["ping", "-n" if is_windows else "-c", "4", target]

        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                check=False,
                text=True,
                timeout=8,
            )
        except subprocess.TimeoutExpired:
            return JsonResponse({"error": "Ping timed out."}, status=408)

        output = completed.stdout + completed.stderr
        times = [int(value) for value in re.findall(r"time[=<](\d+)ms", output, re.IGNORECASE)]
        transmitted = 4
        received = len(times)
        packet_loss = int(((transmitted - received) / transmitted) * 100)

        if times:
            min_latency = min(times)
            avg_latency = round(sum(times) / len(times), 2)
            max_latency = max(times)
        else:
            min_latency = avg_latency = max_latency = None

        return JsonResponse(
            {
                "target": target,
                "packet_loss": packet_loss,
                "min_latency": min_latency,
                "avg_latency": avg_latency,
                "max_latency": max_latency,
                "packets": [
                    {"index": index + 1, "success": True, "time": time}
                    for index, time in enumerate(times)
                ],
                "raw": output,
            }
        )
