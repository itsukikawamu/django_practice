import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Channel, Video, Comment

#test_models

class ChannelModelTest(TestCase):
    def test(self):
        self.assertIs()
    
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
        
        
    
    
    
    