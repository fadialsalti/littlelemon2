from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer

class MenuItemsViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_create_menu_item(self):
        data = {"title": "Burger", "price": 7.99, "inventory": 75}
        response = self.client.post(reverse("menu"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class SingleMenuItemViewTestCase(APITestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            title="Pizza", price=9.99, inventory=100
        )
        self.client = APIClient()

    # def test_retrieve_menu_item(self):
    #     response = self.client.get('/restaurant/menu', kwargs={"pk": self.menu.pk})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['title'], 'Pizza')

    # def test_update_menu_item(self):
    #     data = {"title": "Pizza", "price": 10.99, "inventory": 150}
    #     response = self.client.put(reverse("menu-detail", kwargs={"pk": self.menu.pk}), data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delete_menu_item(self):
    #     response = self.client.delete(reverse("menu-detail", kwargs={"pk": self.menu.pk}))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BookingViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.booking = Booking.objects.create(
            name='Test Booking',
            no_of_guests=2,
            bookingdate='2022-12-15'
        )

    # def test_list_bookings(self):
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.get('/restaurant/booking/tables/10')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #     print(response.data)
        #self.assertEqual(response.data[0]['name'], 'Test Booking')

    # def test_create_booking(self):
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.post(
    #         '/api/bookings/',
    #         {
    #             'name': 'Test Booking 2',
    #             'no_of_guests': 4,
    #             'bookingdate': '2022-12-16'
    #         },
    #         format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Booking.objects.count(), 2)

    # def test_retrieve_booking(self):
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.get('/api/bookings/1/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['name'], 'Test Booking')

    # def test_update_booking(self):
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.put(
    #         '/api/bookings/1/',
    #         {
    #             'name': 'Updated Test Booking',
    #             'no_of_guests': 4,
    #             'bookingdate': '2022-12-16'
    #         },
    #         format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['name'], 'Updated Test Booking')
    #     self.assertEqual(Booking.objects.get(id=1).name, 'Updated Test Booking')

    # def test_delete_booking(self):
    #     self.client.force_authenticate(user=self.user)
    #     response = self