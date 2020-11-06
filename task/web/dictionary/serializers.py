from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    category = serializers.CharField()
    level = serializers.CharField()
    theme = serializers.CharField()
    stw = serializers.CharField()
    user_id = serializers.IntegerField()
    example = serializers.CharField()
    transcription = serializers.CharField()

    def create(self, validated_data):
        return Word.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.level = validated_data.get('level', instance.level)
        instance.theme = validated_data.get('theme', instance.theme)
        instance.stw = validated_data.get('stw', instance.stw)
        instance.theme = validated_data.get('example', instance.example)
        instance.stw = validated_data.get('transcription', instance.transcription)
        instance.user_id = validated_data.get('user_id', instance.user_id)

        instance.save()
        return instance
