# serializers.py
from rest_framework import serializers

from .models import Video

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('title','description','thumbnailURL','PublishedOn','timeStamp')