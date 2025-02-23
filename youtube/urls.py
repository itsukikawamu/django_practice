from django.urls import path

from . import views

app_name = "youtube"
urlpatterns = [
    path("", views.home, name="home"),
    path("<str:channel_name>/", views.channel, name = "channel")
]