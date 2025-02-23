from django.urls import path

from . import views

app_name = "youtube"
urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:channel_slug>/", views.channel, name = "channel")
]