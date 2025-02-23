from django.http import HttpResponse
from django.shortcuts import render
from .models import Channel

def home(request):
    channel_list = Channel.objects.order_by("-subscribers_number")[:5]
    context = {
        "channel_list": channel_list
    }
    return render(request, "youtube/home.html", context)