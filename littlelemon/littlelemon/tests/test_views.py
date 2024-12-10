from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializer import MenuSerializer, BookingSerializer
from datetime import date

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(name="pizza", price=10)
        
    def get_test(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        self.assertEqual(len(serialized_items.data), 1)
        
class BookingViewTest(TestCase):
    def setup(self):
        Booking.objects.create(name="marselia", data=date.today())
        
    def get_test(self):
        items = Booking.objects.all()
        serializerd_items = BookingSerializer(items, many=True)
        self.assertEqual(len(serializerd_items.data), 1)