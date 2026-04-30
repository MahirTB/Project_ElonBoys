from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('index.html', HomeView.as_view(), name='home-alias'),
    path('members/', MemberView.as_view(), name='member-view'),
    path('member.html', MemberView.as_view(), name='member-alias'),
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('activities/', ActivitiesView.as_view(), name='activities'),
    path('resources/', ResourcesView.as_view(), name='resources'),
    path('photos/', PhotosView.as_view(), name='photos'),
    path('tools/', ToolsView.as_view(), name='tools'),
    path('tools/ping/', PingToolView.as_view(), name='ping-tool'),
]
