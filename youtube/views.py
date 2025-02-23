from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Channel

def home(request):
    channel_list = Channel.objects.order_by("-subscribers_number")[:5]
    context = {
        "channel_list": channel_list
    }
    return render(request, "youtube/home.html", context)

def channel(request, channel_name):
    channel = get_object_or_404(Channel, name=channel_name)
    context = {
        "channel": channel
    }
    return render(request, "youtube/channel.html", context)