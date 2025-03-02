import time
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Channel, Video

def home(request):
    channel_list = Channel.objects.order_by("-subscribers_number")[:5]
    video_list = Video.objects.order_by("-like_number")[:10]
    context = {
        "channel_list": channel_list,
        "video_list": video_list
    }
    return render(request, "youtube/home.html", context)

def video(request, channel_slug, video_slug):
    channel = get_object_or_404(Channel, slug=channel_slug)
    video = get_object_or_404(Video, slug=video_slug, channel=channel)
    context = {
        "video": video
    }
    return render(request, "youtube/video.html", context)

class ChannelView(generic.ListView):
    model = Video
    template_name = "youtube/channel.html"
    context_object_name = "video_list"
    
    def get_queryset(self):
        self.channel = get_object_or_404(Channel, slug=self.kwargs["channel_slug"])
        return self.channel.video_set.order_by("-uploaded_at")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["channel"] = self.channel
        context["channel_slug"] = self.channel.slug
        return context
