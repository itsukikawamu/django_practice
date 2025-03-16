from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils.text import slugify
from youtube.models import Channel


class Command(BaseCommand):
    help = "slugが空のchannelにslugify(channel.name)を適用する"
    def handle(self, *args, **kwargs):
        channels = Channel.objects.filter(Q(slug__isnull=True) | Q(slug=""))
        
        for channel in channels:
            channel.slug = slugify(channel.name)
            channel.save()
        
        self.stdout.write(self.style.SUCCESS(f"{channels.count()} 件のchannel_slugを更新しました"))
        
        
        
        
        
        
        
        
        
        