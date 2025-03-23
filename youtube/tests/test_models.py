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
        IntegrityError occurrs.
        """
        try:
            create_channel()
        except (IntegrityError):
            pass
        else:
            self.fail()
    
    def test_blank_name_channel(self):
        """
        created channel with blank in name, 
        ValidationError occurrs.
        """
        channel = Channel(name="")
        with self.assertRaises(ValidationError):
            channel.full_clean()
            
    def test_name_max_length_exceeded(self):
        """
        Name should not exceed the max_length of 225.
        """
        long_name = "A" * 226
        channel = Channel(name=long_name)
        with self.assertRaises(ValidationError):
            channel.full_clean()
    
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
        with self.assertRaises(IntegrityError):
            Video.objects.create(channel=None, title="null channel video")
            
    def test_video_with_non_existent_channel(self):
        """
        Creating a Video with a non-existent Channel in DB,
        IntegrityError occers.
        """
        non_exist_id = 9999
        video = Video(title="test", channel_id=non_exist_id)
        with self.assertRaises(ValidationError):
            video.full_clean()
    
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
        IntegrityError occurrs.
        """
        with self.assertRaises(IntegrityError):
            create_video()
    
    def test_blank_title_video(self):
        """
        created video with blank title, 
        ValidationError occurrs.
        """
        video = Video(title="")
        with self.assertRaises(ValidationError):
            video.full_clean()
            
    def test_name_max_length_exceeded(self):
        """
        Name should not exceed the max_length of 225.
        """
        long_name = "A" * 226
        video = Video(title=long_name)
        with self.assertRaises(ValidationError):
            video.full_clean()
    
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
        
    def test_slug_max_length_exceeded(self):
        """
        Slug should not exceed max_length of 255.
        """
        long_title = "A" * 300
        video = create_video(long_title)
        self.assertLessEqual(len(video.slug), 255) 
        
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
    
    def test_get_embed_url_with_valid_url(self):
        """
        get_embed_url() should convert watch?v= to embed/ in external_url.
        """
        video = create_video("test")
        video.external_url = "https://www.youtube.com/watch?v=abcd1234"
        self.assertEqual(video.get_embed_url(), "https://www.youtube.com/embed/abcd1234")
    
    def test_get_embed_url_without_external_url(self):
        """
        get_embed_url() should return None if external_url is not set.
        """
        video = create_video("test")
        self.assertIsNone(video.get_embed_url())
    
    def test_invalid_external_url(self):
        """
        Invalid URL should raise ValidationError.
        """
        video = create_video("test")
        video.external_url = "invalid-url"
        with self.assertRaises(ValidationError):
           video.full_clean()
    
    def test_view_count_defaults_to_zero(self):
        """
        view_count defaults to zero.
        """
        video = create_video("test")
        self.assertEqual(video.view_count, 0)

    def test_view_count_cant_be_negative(self):
        video = create_video("test")
        with self.assertRaises(ValidationError): 
            video.view_count = -1000
            video.full_clean()

    
    def test_like_count_defaults_to_zero(self):
        """
        like_count defaults to zero.
        """
        video = create_video("test")
        self.assertEqual(video.like_count, 0)

    def test_like_count_cant_be_negative(self):
        video = create_video("test")
        with self.assertRaises(ValidationError): 
            video.like_count = -1000
            video.full_clean()


def create_comment(text=None, video=None):
    if not video:
        video = create_video("test")
    comment = Comment.objects.create(text=text, video=video)
    return comment
    
class CommentModelTest(TestCase):
    databases = {"default", "youtube_db"}
    
    def test_Comment_with_null_video(self):
        """
        created Comment in null video, 
        IntegrityError occers.
        """
        with self.assertRaises(IntegrityError):
            Comment.objects.create(video=None, text="null video Comment")
            
    def test_Comment_with_non_existent_video(self):
        """
        Creating a Comment with a non-existent Video in DB,
        IntegrityError occers.
        """
        non_exist_video_id = 9999
        comment = Comment(text="test", video_id=non_exist_video_id)
        with self.assertRaises(ValidationError):
            comment.full_clean()
    
    def test_Comment_deleted_when_video_deleted(self):
        """
        When a video is deleted, its related Comments should also be deleted.
        """
        comment = create_comment("test")
        self.assertEqual(Comment.objects.count(), 1)
        comment_pk = comment.pk
        comment.video.delete()
        self.assertFalse(Comment.objects.filter(pk=comment_pk).exists())
        self.assertEqual(Comment.objects.count(), 0)
    
    def test_null_text_comment(self):
        """
        created comment without text, 
        IntegrityError occurrs.
        """
        with self.assertRaises(IntegrityError):
            create_comment()
    
    def test_blank_text_comment(self):
        """
        created comment with blank text, 
        ValidationError occurrs.
        """
        comment = Comment(text="")
        with self.assertRaises(ValidationError):
            comment.full_clean()
            
    def test_name_max_length_exceeded(self):
        """
        Name should not exceed the max_length of 225.
        """
        long_name = "A" * 1001
        comment = Comment(text=long_name)
        with self.assertRaises(ValidationError):
            comment.full_clean()