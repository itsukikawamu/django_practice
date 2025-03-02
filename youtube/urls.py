from django.urls import path

from . import views

app_name = "youtube"
urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:channel_slug>/", views.ChannelView.as_view(), name = "channel"),
    path("<slug:channel_slug>/<slug:video_slug>/", views.video, name="video"),
]