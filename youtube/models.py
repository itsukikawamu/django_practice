from django.db import models
from django.utils.text import slugify

class Channel(models.Model):
    name = models.CharField(max_length=225, blank=False)
    slug = models.SlugField(max_length=225, unique=True, editable=False)
    subscribers_number = models.PositiveBigIntegerField(verbose_name="登録者数", default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            
            counter = 1
            while Channel.objects.filter(slug=unique_slug).exists():
                unique_slug  = f"{base_slug}-{counter}"
                counter += 1
                
            self.slug = unique_slug
        
        else:
            self.slug = Channel.objects.get(pk=self.pk).slug
        
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
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