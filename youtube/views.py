from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from django.views.decorators.http import require_POST
from django.db.models import F
from .models import Channel, Video, Comment 
from .forms import SearchForm, ContactForm
import json
        

class HomeView(generic.TemplateView):
    template_name = "youtube/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel_list"] = Channel.objects.order_by("-subscribers_number")[:5]
        context["video_list"] = Video.objects.order_by("-like_count")[:10]
        
        form = SearchForm(self.request.GET or None)
        context["form"] = form
        if form.is_valid():
            keyword = form.cleaned_data["keywords"]
            context["video_list"] = Video.objects.filter(title__icontains=keyword)
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
        context["video_list"] = Video.objects.order_by("-like_count")[:10]
        
        video = context["video"]
        video.view_count = F("view_count") + 1
        video.save(update_fields=["view_count"])
        video.refresh_from_db()
        
        return  context

@require_POST
def evaluate_video(request, channel_slug, video_slug):
    channel=get_object_or_404(Channel, slug=channel_slug)
    video = get_object_or_404(Video, channel=channel, slug=video_slug)
    
    video.like_count = F("like_count") + 1
    video.save(update_fields=["like_count"])
    video.refresh_from_db()
    return JsonResponse({"success": True, "like_count": video.like_count})

@require_POST
def comment(request, channel_slug, video_slug):
    channel=get_object_or_404(Channel, slug=channel_slug)
    video = get_object_or_404(Video, channel=channel, slug=video_slug)
    data = json.loads(request.body)
    new_comment = Comment.objects.create(video=video, text=data.get("commentText"))
    return JsonResponse({"success": True, "newCommentText": new_comment.text}, status=201)

    
@require_POST
def subscribe(request, channel_slug):
    channel = get_object_or_404(Channel, slug=channel_slug)
    channel.subscribers_number = F("subscribers_number") + 1
    channel.save(update_fields=["subscribers_number"])
    channel.refresh_from_db()
    return JsonResponse({"success": True, "subscribers_number": channel.subscribers_number})

    
class ContactView(generic.TemplateView):
    template_name="youtube/contact.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ContactForm(self.request.GET or None)
        context["form"] = form
        return context
    