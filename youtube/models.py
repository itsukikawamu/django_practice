from django.db import models

class Channel(models.Model):
    Channel_name = models.CharField(max_length=200)