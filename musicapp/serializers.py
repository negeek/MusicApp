from rest_framework import serializers
from .models import Artiste, Lyric, Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id', 'title', 'date_released', 'likes', 'artiste_id')
        model = Song

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            'title', instance.title)
        instance.date_released = validated_data.get(
            'date_released', instance.date_released)
        instance.likes = validated_data.get(
            'likes', instance.likes)
        instance.artiste_id = validated_data.get(
            'artiste_id', instance.artiste_id)
        instance.save()
        return instance


class ArtisteSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id', 'first_name', 'last_name', 'age')
        model = Artiste

    def create(self, validated_data):
        return Artiste.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.age = validated_data.get(
            'age', instance.age)
        instance.save()
        return instance


class LyricSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id', 'content', 'song_id')
        model = Lyric

    def create(self, validated_data):
        return Lyric.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get(
            'content', instance.content)
        instance.song_id = validated_data.get(
            'song_id', instance.song_id)
        instance.save()
        return instance
