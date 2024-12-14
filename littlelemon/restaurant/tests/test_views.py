from django.test import TestCase, SimpleTestCase
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer
from django.urls import reverse

class MenuViewTest(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/restaurant/')
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_uses_correct_template(self):
        response = self.client.get('/restaurant/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_homepage_contains_welcome_message(self):
        response = self.client.get('/restaurant/')
        self.assertContains(response, 'Welcome to our Store!')
        
class TestMenuPage(TestCase):
    """Create some menus for testing"""
    def setUp(self):
        Menu.objects.create(title="sahlab", price=20, inventory=100)
    def test_menus_uses_correct_template(self):
        response = self.client.get(reverse('menus'))
        self.assertTemplateUsed(response, 'menu.html')
    def test_menus_context(self):
        response = self.client.get(reverse('menus'))
        self.assertEqual(len(response.context['menus']), 1)
        self.assertContains(response, 'sahlab')
        self.assertNotContains(response, 'No products available')
        
class TestMenu(TestCase):
    def setUp(self):
        Menu.objects.create(title="Nana", price=10, inventory=20)
    
    def test_get_all(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        self.assertEqual(len(serialized_items.data), 1)