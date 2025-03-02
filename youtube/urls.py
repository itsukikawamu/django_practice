from django.urls import path

from . import views

app_name = "youtube"
urlpatterns = [
    path("", views.home, name="home"),
    path("sleeper", views.sleeper, name="sleeper"),
    path("trending/", views.trending, name="trending"),
    path("my_channel/", views.MyChannelView.as_view(), name = "my_channel"),
    path("<slug:channel_slug>/", views.ChannelView.as_view(), name = "channel"),
    path("<slug:channel_slug>/<slug:video_slug>/", views.video, name="video"),
]