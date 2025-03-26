from django.contrib import admin

from .models import Channel, Video, Comment, Contact

admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Contact)