from django.urls import path
from . import views

app_name = "youtube"
urlpatterns = [

    path("", views.HomeView.as_view(), name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("<slug:channel_slug>/", views.ChannelView.as_view(), name = "channel"),
    path("<slug:channel_slug>/<slug:video_slug>/", views.VideoView.as_view(), name="video"),
    path("<slug:channel_slug>/<slug:video_slug>/evaluate", views.evaluate_video, name="evaluate"),
    path("<slug:channel_slug>/<slug:video_slug>/comment", views.comment, name="comment"),
    path("<slug:channel_slug>/subscribe", views.subscribe, name="subscribe"),
]