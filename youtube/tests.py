import datetime

from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.utils import timezone 
from django.utils.text import slugify
from django.urls import reverse

from .models import Channel, Video, Comment

#test_models

class ChannelModelTest(TestCase):
    databases = {"default", "youtube_db"}
    
    def test_null_name_channel(self):
        """
        created channel without name, 
        ValidationError occurrs.
        """
        try:
            Channel.objects.create()
        except (IntegrityError, ValidationError):
            pass
        else:
            self.fail()
    
    def test_blank_name_channel(self):
        """
        created channel with blank in name, 
        ValidationError occurrs.
        """
        with self.assertRaises(ValidationError):
            Channel.objects.create(name="")
    
    def test_valid_name(self):
        """
        created channel with valid name,
        """
        ch_name = "Test Channel"
        channel = Channel.objects.create(name=ch_name)
        self.assertIsNotNone(channel.pk)
        self.assertEqual(channel.name, ch_name)

        
"""
    def test_ch_slug_generate(self):
        channel = Channel.objects.create("Test Channel")
        self.assertEqual(channel.slug, "test-channel")
"""
  

"""    
class VideoModelTest(TestCase):
    def test(self):
        self.assertIs()
        
class CommentModelTest(TestCase):
    def test(self):
        self.assertIs()
        
#test_views

class HomeViewTest(TestCase):
    def test(self):
        response = self.client.get(reverse("youtube:home"))
        self.assertEqual(response.status_code, 200)
        
class ChannelViewTest(TestCase):
    def test(self):
        response = self.client.get(reverse("youtube:channel"))
        self.assertEqual(response.status_code, 200)
    
class VideoViewTest(TestCase):
    def test(self):
        response = self.client.get(reverse("youtube:video"))
        self.assertEqual(response.status_code, 200)


class EvaluateViewTest(TestCase):
    def test(self):
        response = self.client.post(reverse("youtube:evaluate"))
        self.assertEqual(response.status_code, 200)

class CommentViewTest(TestCase):
    def test(self):
        response = self.client.post(reverse("youtube:comment"))
        self.assertEqual(response.status_code, 201)
"""
        
    
    
    
    