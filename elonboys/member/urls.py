from django.urls import path
from .views import *


urlpatterns = [
    path('member/', MemberView.as_view(), name='member-view'),
]