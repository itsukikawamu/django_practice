from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from django.db.models import F
from .models import Channel, Video, Comment 
import json
        

class HomeView(generic.TemplateView):
    template_name = "youtube/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel_list"] = Channel.objects.order_by("-subscribers_number")[:5]
        context["video_list"] = Video.objects.order_by("-likes")[:10]
        return context
    
class ChannelView(generic.ListView):
    template_name = "youtube/channel.html"
    model = Video
    context_object_name = "video_list"
   
    def get_queryset(self):
        self.channel = get_object_or_404(Channel, slug=self.kwargs["channel_slug"])
        return Video.objects.filter(channel=self.channel).order_by("-uploaded_at")
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel"] = get_object_or_404(Channel, slug=self.kwargs.get("channel_slug"))
        return context

class VideoView(generic.TemplateView):
    template_name = "youtube/video.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel"] = get_object_or_404(Channel, slug=kwargs["channel_slug"])
        context["video"] = get_object_or_404(Video, slug=kwargs["video_slug"], channel=context["channel"])
        context["comment_list"] = Comment.objects.filter(video=context["video"]).order_by("-uploaded_at")
        
        return  context

class EvaluateView(View):
    def post(self, request, *args, **kwargs):
        channel=get_object_or_404(Channel, slug=kwargs["channel_slug"])
        video = get_object_or_404(Video, channel=channel, slug=kwargs["video_slug"])
        
        video.likes = F("likes") + 1
        video.save(update_fields=["likes"])
        video.refresh_from_db()
        return JsonResponse({"success": True, "likes": video.likes})

class CommentView(View):
    def post(self, request, *args, **kwargs):
        channel=get_object_or_404(Channel, slug=kwargs["channel_slug"])
        video = get_object_or_404(Video, channel=channel, slug=kwargs["video_slug"])
        data = json.loads(request.body)
        new_comment = Comment.objects.create(video=video, text=data.get("commentText"))
        return JsonResponse({"success": True, "newCommentText": new_comment.text}, status=201)
    
    
    