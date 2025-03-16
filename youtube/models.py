from django.db import models
from django.utils.text import slugify

class Channel(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, unique=True, blank=True)
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
    slug = models.SlugField(unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    external_url = models.URLField(blank=True, null=True)
    likes = models.IntegerField(verbose_name="likes", default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kargs)
    
    def get_embed_url(self):
        if self.external_url:
            return self.external_url.replace("watch?v=", "embed/")
        return None
    
    def get_comments(self):
        return self.comments.order_by("-uploaded_at")
    
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    uploaded_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text[:30]}"