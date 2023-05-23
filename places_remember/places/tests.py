from django.test import TestCase
from django.contrib.auth.models import User
from .models import Place


class PlaceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creating a user to connect to a place
        cls.user = User.objects.create(username='testuser')

        # Creating a test location
        cls.place = Place.objects.create(
            user=cls.user,
            name='Test Place',
            comment='This is a test place',
            location='Test Location'
        )

    def test_str_representation(self):
        self.assertEqual(str(self.place), 'testuser')

    def test_place_attributes(self):
        self.assertEqual(self.place.user, self.user)
        self.assertEqual(self.place.name, 'Test Place')
        self.assertEqual(self.place.comment, 'This is a test place')
        self.assertEqual(self.place.location, 'Test Location')

