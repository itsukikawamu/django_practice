from django.urls import path

from . import views

app_name = "youtube"
urlpatterns = [
    path("", views.home, name="home"),
    path("trending/", views.trending, name="trending"),
    path("<slug:channel_slug>/", views.channel, name = "channel"),
    path("<slug:channel_slug>/<slug:video_slug>/", views.video, name="video"),
]