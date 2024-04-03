from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from .models import Member
# Create your views here.


class MemberView(View):
    def get(self,request):
        members = Member.objects.all()
        return render (request,"member.html",{"members":members})
