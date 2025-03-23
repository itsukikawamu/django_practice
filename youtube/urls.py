from django.urls import path
from . import views

app_name = "youtube"
urlpatterns = [

    path("", views.HomeView.as_view(), name="home"),
    path("<slug:channel_slug>/", views.ChannelView.as_view(), name = "channel"),
    path("<slug:channel_slug>/<slug:video_slug>/", views.VideoView.as_view(), name="video"),
    path("<slug:channel_slug>/<slug:video_slug>/evaluate", views.EvaluateView.as_view(), name="evaluate"),
    path("<slug:channel_slug>/<slug:video_slug>/comment", views.CommentView.as_view(), name="comment"),
    path("<slug:channel_slug>/subscribe", views.SubscribeView.as_view(), name="subscribe"),
]