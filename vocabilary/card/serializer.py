from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['pk', 'english', 'russian', 'new_card', 'remembered', 'part_of_speech', 'repeat']
