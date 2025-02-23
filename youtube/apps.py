from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command

class YoutubeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtube'
    
    def ready(self):
        post_migrate.connect(migrate_youtube, sender=self)
        
def migrate_youtube(sender, **kwargs):
    if kwargs.get("using") == "youtube_db":
        return
    call_command("migrate", database="youtube_db")