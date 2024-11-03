from django.test import TestCase

from firstapp.serializers import MovieSerializer


class TestMovieSerializer(TestCase):
    def setUp(self):
        self.serializer = MovieSerializer()