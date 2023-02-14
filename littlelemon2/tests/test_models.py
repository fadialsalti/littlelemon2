from django.test import TestCase
from django.utils import timezone
from restaurant.models import Menu, Booking

class MenuModelTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(title='Burger', price=9.99, inventory=10)
        self.assertEqual(str(menu), 'Burger')

    def test_menu_price(self):
        menu = Menu.objects.create(title='Burger', price=9.99, inventory=10)
        self.assertEqual(menu.price, 9.99)
        
    def test_menu_inventory(self):
        menu = Menu.objects.create(title='Burger', price=9.99, inventory=10)
        self.assertEqual(menu.inventory, 10)

class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(name='John Doe', no_of_guests=4, bookingdate=timezone.now().date())
        self.assertEqual(booking.name, 'John Doe')
    
    def test_no_of_guests(self):
        booking = Booking.objects.create(name='John Doe', no_of_guests=4, bookingdate=timezone.now().date())
        self.assertEqual(booking.no_of_guests, 4)
        
    def test_booking_date(self):
        booking_date = timezone.now().date()
        booking = Booking.objects.create(name='John Doe', no_of_guests=4, bookingdate=booking_date)
        self.assertEqual(booking.bookingdate, booking_date)
