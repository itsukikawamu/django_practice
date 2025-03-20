import datetime

from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.utils import timezone 
from django.utils.text import slugify
from django.urls import reverse

from ..models import Channel, Video, Comment

def create_channel(name=None):
    channel = Channel.objects.create(name=name)
    return channel

class ChannelModelTest(TestCase):
    databases = {"default", "youtube_db"}
    
    def test_null_name_channel(self):
        """
        created channel without name, 
        ValidationError occurrs.
        """
        try:
            create_channel()
        except (ValidationError):
            pass
        else:
            self.fail()
    
    def test_blank_name_channel(self):
        """
        created channel with blank in name, 
        ValidationError occurrs.
        """
        with self.assertRaises(ValidationError):
            create_channel("")
            
    def test_name_max_length_exceeded(self):
        """
        Name should not exceed the max_length of 225.
        """
        long_name = "A" * 226
        with self.assertRaises(ValidationError):
            create_channel(long_name)
    
    def test_valid_name(self):
        """
        created channel with valid name,
        """
        ch_name = "Test Channel"
        channel = create_channel(ch_name)
        self.assertIsNotNone(channel.pk)
        self.assertEqual(channel.name, ch_name)

    def test_ch_nomal_slug_generate(self):
        """
        slug generated slugified from channel name.
        """
        ch_name = "slug generate Channel"
        channel = create_channel(ch_name)
        self.assertEqual(channel.slug, slugify(ch_name))
        
    def test_ch_special_slug_generate(self):
        """
        slugify from channel name with special characters.
        """
        ch_name = "Test !@#$  %^&*()こんにちは Channel"
        channel = create_channel(ch_name)
        self.assertEqual(channel.slug, slugify(ch_name))
        
    def test_ch_slug_generate_with_duplicated(self):
        """
        Generate numbered slugs in case of duplicate channel names
        """
        ch_name = "Duplicated Channel"
        channels = [create_channel(ch_name) for _ in range(5)]
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
        channel = create_channel(ch_name)
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
        channel = create_channel(ch_name)
        self.assertEqual(channel.subscribers_number, 0)

    def test_subscribers_cant_be_negative(self):
        channel = create_channel("test")
        with self.assertRaises(ValidationError): 
            channel.subscribers_number = -1000
            channel.full_clean()

def create_video(title=None, channel=None):
    if not channel:
        channel = create_channel(name="test")
    video = Video.objects.create(channel=channel, title=title)
    return video

class VideoModelTest(TestCase):
    databases = {"default", "youtube_db"}
    
    def test_video_with_null_channel(self):
        """
        created video in null channel, 
        IntegrityError occers.
        """
        with self.assertRaises(ValidationError):
            Video.objects.create(channel=None, title="null channel video")
            
    def test_video_with_non_existent_channel(self):
        """
        Creating a Video with a non-existent Channel in DB,
        IntegrityError occers.
        """
        non_exist_channel_id = 9999

        with self.assertRaises(ValidationError):
            Video.objects.create(title="Invalid Channel Video", channel_id=non_exist_channel_id)
    
    def test_video_deleted_when_channel_deleted(self):
        """
        When a Channel is deleted, its related Videos should also be deleted.
        """
        video = create_video("test")
        self.assertEqual(Video.objects.count(), 1)
        video_pk = video.pk
        video.channel.delete()
        self.assertFalse(Video.objects.filter(pk=video_pk).exists())
        self.assertEqual(Video.objects.count(), 0) 
    
    def test_null_title_video(self):
        """
        created video without title, 
        ValidationError occurrs.
        """
        with self.assertRaises(ValidationError):
            create_video()
    
    def test_blank_title_video(self):
        """
        created video with blank title, 
        ValidationError occurrs.
        """
        with self.assertRaises(ValidationError):
            create_video("")
            
    def test_name_max_length_exceeded(self):
        """
        Name should not exceed the max_length of 225.
        """
        long_name = "A" * 226
        with self.assertRaises(ValidationError):
            create_video(long_name)
    
    def test_valid_name(self):
        """
        created channel with valid name,
        """
        title = "Test  Video"
        video = create_video(title)
        self.assertIsNotNone(video.pk)
        self.assertEqual(video.title, title)

    def test_video_nomal_slug_generate(self):
        """
        slug generated slugified from video title.
        """
        title="slug generate video"
        video = create_video(title)
        self.assertEqual(video.slug, slugify(title))
        
    def test_ch_special_slug_generate(self):
        """
        slugify from video title with special characters.
        """
        title = "Test !@#$  %^&*()こんにちは Video"
        video = create_video(title)
        self.assertEqual(video.slug, slugify(title))
        
    def test_ch_slug_generate_with_duplicated(self):
        """
        Generate numbered slugs in case of duplicate video titles
        """
        title = "Duplicated Channel"
        videos = [create_video(title) for _ in range(5)]
        for i, video in enumerate(videos):
            self.assertIsNotNone(video.pk)
            
            if i == 0:
                self.assertEqual(video.slug, slugify(title))
            else:    
                self.assertEqual(video.slug, f"{slugify(title)}-{i}")

    def test_slug_isnt_changed(self):
        """
        slug is not changeable.
        """
        title = "slug unchangeable channel"
        video = create_video(title)
        first_slug = video.slug
        video.title = "changed channel name"
        video.slug = slugify(video.title)
        video.save()
        self.assertEqual(video.slug, first_slug)

"""
class CommentModelTest(TestCase):
"""