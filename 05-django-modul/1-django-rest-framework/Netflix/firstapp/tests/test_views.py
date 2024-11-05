# # from django.test import TestCase, Client
# #
# # from firstapp.models import Actor
# #
# #
# # class TestActorViewSet(TestCase):
# #     def setUp(self):
# #         self.actor = Actor.objects.create(name='Test Actor')
# #         self.client = Client()
# #
# #     def test_actor_list(self):
# #         response = self.client.get('/actors/')
# #         data = response.data
# #
# #         self.assertEquals(response.status_code, 200)
# #         self.assertEquals(len(data), 1)
# #         self.assertIsNotNone(data[0]['id'])
# #         self.assertEquals(data[0]['name'], 'Test Actor')
#
#
# from django.test import TestCase, Client
# from firstapp.models import Actor
#
#
# class TestActorViewSet(TestCase):
#     def setUp(self):
#         self.actor = Actor.objects.create(
#             name='Test Actor',
#             birthdate='2005-03-05',  # Example date
#             gender='M'               # Example gender
#         )
#         self.client = Client()
#
#     def test_actor_list(self):
#         response = self.client.get('/actors/')
#         data = response.data
#
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(len(data), 1)
#         self.assertIsNotNone(data[0]['id'])
#         self.assertEquals(data[0]['name'], 'Test Actor')


from django.test import TestCase, Client
from firstapp.models import Actor


class TestActorViewSet(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(
            name='Test Actor',
            birthdate='2005-03-05',  # Example date
            gender='M'  # Example gender
        )
        self.client = Client()

    def test_actor_list(self):
        response = self.client.get('/actors/')
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected structure
        data = response.json()  # Use .json() to parse JSON response
        print("Response Data:", data)  # Debugging line

        self.assertEqual(len(data), 1)
        self.assertIn('id', data[0])  # Check if 'id' exists
        self.assertEqual(data[0]['name'], 'Test Actor')
