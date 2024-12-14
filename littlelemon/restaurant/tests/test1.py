from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.tea = Men
        