from django.contrib import admin

from .models import Channel, Video, Comment

admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Comment)