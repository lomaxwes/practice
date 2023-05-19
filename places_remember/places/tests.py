from django.test import TestCase
from django.contrib.auth.models import User
from .models import Place


class PlaceTestCase(TestCase):
    def setUp(self):
        # Creating a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_place(self):
        # Creating a new impression of the place visited
        place = Place.objects.create(user=self.user, name='Test Place', comment='Test Comment')

        # Check that the impression has been successfully created
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.comment, 'Test Comment')
        self.assertEqual(place.user, self.user)

    def test_get_place_list(self):
        # Creating a few impressions about the places visited
        Place.objects.create(user=self.user, name='Place 1', comment='Comment 1')
        Place.objects.create(user=self.user, name='Place 2', comment='Comment 2')

        # We get a list of impressions about the places visited
        places = Place.objects.filter(user=self.user)

        # Check that the list contains the expected number of items
        self.assertEqual(places.count(), 2)

        # Check that the list items match the expected values
        self.assertEqual(places[0].name, 'Place 1')
        self.assertEqual(places[0].comment, 'Comment 1')
        self.assertEqual(places[1].name, 'Place 2')
        self.assertEqual(places[1].comment, 'Comment 2')

