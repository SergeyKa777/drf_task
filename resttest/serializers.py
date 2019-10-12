from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Game, Probe, Ss, Track, Album
from django.db.models import Q
from django.db import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'description']


class GameSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'description']


class ProbeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Probe
        fields = ['t1', 'desc']


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ss
        fields = ['id', 'name']


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ss
        fields = ['id', 'name']



#class SsSerializer(serializers.ModelSerializer):
#    parent = serializers.SerializerMethodField()
#    children = ChildSerializer(many=True)
#    class Meta:
#        model = Ss
#        fields = ('id', 'name', 'parent','children')
#
#
#    def get_parent(self, obj):
#        if obj.parent is not None:
#            return SsSerializer(obj.parent).data
#        else:
#            return None
#
#    def create(self, validated_data):
#
#
#        print(validated_data)
#        tracks_data = validated_data.pop('children')
#        print(tracks_data)
#
#        name = Ss.objects.create(**validated_data)
#        print(name)
#        for tra in tracks_data:
#            print(tra)
#            Ss.objects.create(name=name)
#        return name



#
#
class SsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ss
        fields = ('name', 'children')

    def create(self, validated_data):
        children = validated_data.pop('children', [])
        node = Ss.objects.create(
            parent=self.context.get('parent'),
            **validated_data)
        for child_data in children:
            s = SsSerializer(data=child_data, context={'parent': node})
            s.is_valid(raise_exception=True)
            s.save()
        return node

    def to_representation(self, instance):
        if not isinstance(instance, models.Model):
            return instance
        else:
            representation = super(SsSerializer, self).to_representation(instance)

            ### На этом мои познания закончились )))
            representation['parents'] = [ChildSerializer(child).data
                                         for child in instance.children.all()]


            representation['children'] = [ChildSerializer(child).data
                                          for child in instance.children.all()]


            representation['siblings'] = [ChildSerializer(child).data
                                          for child in instance.children.all()]

            return representation

    def validate(self, data):
        children = self.initial_data.get('children')
        if children:
            self._validate_children(children)
            data.update({'children': children})
        return data

    def _validate_children(self, value):

        pass


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album
