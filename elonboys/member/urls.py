from django.urls import path
from .views import *


urlpatterns = [
    path('members/', MemberView.as_view(), name='member-view'),
]