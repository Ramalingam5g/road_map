from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.test import TestCase, Client
from django.urls import reverse, resolve
from rest_framework.test import APITestCase, APIClient
from rest_api.views import RoadTypeView, RoadView
from rest_api.models import RoadProperties, RoadType
from rest_api.serializers import RoadPropertiesSerializer, RoadTypeSerializers
# initialize the APIClient app
client = Client()


class RoadTypeViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="admin")
        self.client = APIClient()
        self.login_url = reverse("token_obtain_pair")
        self.roadtype_url = reverse("RoadTypeView")
        self.access_token = self.client.post(
            self.login_url, {"username": "admin", "password": "admin"}
        ).json()["access"]

    def test_login_return_jwt(self):
        credentials = {
            "username": "admin",
            "password": "admin",
        }
        response = self.client.post(self.login_url, credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.json().keys())
        self.assertTrue("refresh" in response.json().keys())

    def test_bad_login_dont_return_jwt(self):
        credentials = {
            "username": "admin",
            "password": "adminfake",
        }
        response = self.client.post(self.login_url, credentials)
        self.assertEqual(response.status_code, 401)

    def test_get_roadtype(self):
        # import pdb;pdb.set_trace()

        expected_response = {"message": "helloworld"}
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer'+ self.access_token)
        # expected_response = {"road_type":"urban"}
        response = self.client.get(self.roadtype_url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_response)

    def test_get_distance(self):
        data = {
            "latitude_1": 13.0629,
            "longitude_1": 80.1948,
            "latitude_2": 13.0405,
            "longitude_2": 80.2503,
        }
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer'+ self.access_token)
        response = self.client.get(self.roadtype_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 6.509791866269829)

    def test_get_attributes(self):
        data = {"road_type": "urban"}
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer'+ self.access_token)
        response = self.client.get(self.roadtype_url)
        self.assertEqual(response.status_code, 200)


    def test_put(self):
        data = {
            "name": "eldamasroad",
            "length": "415.25",
            "width": "4533.25",
            "latitude": "2322.25",
            "longitude": "3422.25",
            "distance": "10",
            "road_type": "highway",
        }
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer'+ self.access_token)
        response = self.client.get(self.road_url)
        self.assertEqual(response.status_code, 200)
