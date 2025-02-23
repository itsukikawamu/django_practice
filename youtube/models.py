from django.db import models

class Channel(models.Model):
    channel_name = models.CharField(max_length=200)
    subscribers_number = models.PositiveBigIntegerField(verbose_name="登録者数", default=0)
    
    def __str__(self):
        return self.channel_name
    
    def get_subscribers_number(self):
        return self.subscribers_number