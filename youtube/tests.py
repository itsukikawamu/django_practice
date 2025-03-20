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
            
    def test_name_max_length_exceeded(self):
        """
        Name should not exceed the max_length of 225.
        """
        long_name = "A" * 226
        with self.assertRaises(ValidationError):
            channel = Channel.objects.create(name=long_name)
    
    def test_valid_name(self):
        """
        created channel with valid name,
        """
        ch_name = "Test Channel"
        channel = Channel.objects.create(name=ch_name)
        self.assertIsNotNone(channel.pk)
        self.assertEqual(channel.name, ch_name)

    def test_ch_nomal_slug_generate(self):
        """
        slug generated slugified from channel name.
        
        """
        ch_name = "slug generate Channel"
        channel = Channel.objects.create(name=ch_name)
        self.assertEqual(channel.slug, slugify(ch_name))
        
    def test_ch_nomal_slug_generate(self):
        """
        slugify from channel name with special characters.
        """
        ch_name = "Test !@#$  %^&*()こんにちは Channel"
        channel = Channel.objects.create(name=ch_name)
        self.assertEqual(channel.slug, slugify(ch_name))
        
    def test_ch_slug_generate_with_duplicated(self):
        """
        Generate numbered slugs in case of duplicate channel names
        """
        ch_name = "Duplicated Channel"
        channels = [Channel.objects.create(name=ch_name) for _ in range(5)]
        for i, channel in enumerate(channels):
            self.assertIsNotNone(channel.pk)
            
            if i == 0:
                self.assertEqual(channel.slug, slugify(ch_name))
            else:    
                self.assertEqual(channel.slug, f"{slugify(ch_name)}-{i}")


    def test_slug_isnt_changed(self):
        """
        slug is not changeable.
        """
        ch_name = "slug unchangeable channel"
        channel = Channel.objects.create(name=ch_name)
        first_slug = channel.slug
        channel.name = "changed channel name"
        channel.slug = slugify(channel.name)
        channel.save()
        self.assertEqual(channel.slug, first_slug)

    def test_subscribers_defaults_to_zero(self):
        """
        subscriber_number defaults to zero.
        """
        ch_name = "default subs num channel"
        channel = Channel.objects.create(name=ch_name)
        self.assertEqual(channel.subscribers_number, 0)

    def test_subscribers_cant_be_negative(self):
        channel = Channel.objects.create(name="negative subs")
        with self.assertRaises(ValidationError): 
            channel.subscribers_number = -1000
            channel.full_clean()
"""
class VideoModelTest(TestCase):
    def test(self):
        self.assertIs()
"""
""" 
class CommentModelTest(TestCase):
    def test(self):
        self.assertIs()
        
"""

"""
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
        
    
    
    
    