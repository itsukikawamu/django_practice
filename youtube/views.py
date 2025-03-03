from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import F
from .models import Channel, Video

class HomeView(generic.TemplateView):
    template_name = "youtube/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel_list"] = Channel.objects.order_by("-subscribers_number")[:5]
        context["video_list"] = Video.objects.order_by("-likes")[:10]
        return context
    
class ChannelView(generic.TemplateView):
    template_name = "youtube/channel.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel"] = get_object_or_404(Channel, slug=kwargs["channel_slug"])
        context["video_list"] = Video.objects.filter(channel=context["channel"]).order_by("-uploaded_at")
        return context
      
class VideoView(generic.TemplateView):
    template_name = "youtube/video.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel"] = get_object_or_404(Channel, slug=kwargs["channel_slug"])
        context["video"] = get_object_or_404(Video, slug=kwargs["video_slug"], channel=context["channel"])
        return  context

class EvaluateView(VideoView):
    def post(self, request, *args, **kwargs):
        channel=get_object_or_404(Channel, slug=kwargs["channel_slug"])
        video = get_object_or_404(Video, channel=channel, slug=kwargs["video_slug"])
        video.likes = F("likes") + 1
        video.save(update_fields=["likes"])
        return redirect("youtube:video", channel_slug=channel.slug, video_slug=video.slug)
    