from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Channel, Video

def home(request):
    channel_list = Channel.objects.order_by("-subscribers_number")[:5]
    context = {
        "channel_list": channel_list
    }
    return render(request, "youtube/home.html", context)

def channel(request, channel_slug):
    channel = get_object_or_404(Channel, slug=channel_slug)
    video_list = channel.video_set.order_by("-uploaded_at")
    context = {
        "channel": channel,
        "video_list": video_list
    }
    return render(request, "youtube/channel.html", context)

def video(request, channel_slug, video_slug):
    channel = get_object_or_404(Channel, slug=channel_slug)
    video = get_object_or_404(Video, slug=video_slug, channel=channel)
    context = {
        "video": video
    }
    return render(request, "youtube/video.html", context)

def trending(request):
    context={
        
    }
    return render(request, "youtube/trending.html", context)