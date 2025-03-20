import datetime

from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.utils import timezone 
from django.utils.text import slugify
from django.urls import reverse

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