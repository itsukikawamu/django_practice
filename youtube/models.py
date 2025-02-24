from django.db import models
from django.utils.text import slugify

class Channel(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(null=True, max_length=225, unique=True, blank=True)
    subscribers_number = models.PositiveBigIntegerField(verbose_name="登録者数", default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_subscribers_number(self):
        return self.subscribers_number
    
class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE) 
    title=models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kargs)
    
    def __str__(self):
        return self.title