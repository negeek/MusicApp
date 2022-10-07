from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Artiste, Song, Lyric
import datetime


class ModelsTests(APITestCase):
    def test_create_list_artiste(self):
        url = reverse('artiste-list')

        data = {'first_name': 'Dee', 'last_name': 'Dan', 'age': 23}
        response = self.client.post(
            url, data, format='json')  # create artiste
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url, format='json')  # list artiste
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_artiste_update_delete(self):
        artiste = Artiste(first_name='Wizzy', last_name='Balogun', age=20)
        artiste.save()
        url = reverse('artiste-detail',  kwargs={'pk': artiste.id})
        data = {'first_name': 'Wizzy', 'last_name': 'Balogun', 'age': 25}

        response = self.client.get(url, format='json')  # retreive artiste
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(
            url, data, format='json')  # update artiste
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)  # delete artiste
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_list_song(self):
        url = reverse('song-list')
        date = datetime.date.today()
        artiste = Artiste(first_name='Wizzy', last_name='Balogun', age=20)
        artiste.save()

        data = {'title': 'Sweet',
                'likes': 23, 'date_released': f"{date}", 'artiste_id': artiste.id}
        response = self.client.post(url, data, format='json')  # create song
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url, format='json')  # list song
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_get_update_delete(self):
        date = datetime.date.today()
        artiste = Artiste(first_name='Wizzy', last_name='Balogun', age=20)
        artiste.save()
        song = Song(title='Baby', likes=23,
                    date_released=date, artiste_id=artiste)
        song.save()

        url = reverse('song-detail',  kwargs={'pk': song.id})
        data = {'title': 'Sweetwine', 'date_released': f"{date}",
                'likes': 29, 'artiste_id': artiste.id}
        response = self.client.get(url, format='json')  # retreive song
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(
            url, data, format='json')  # to update song
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)  # to delete song
