from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from rest_framework import pagination

from .models import *


# Сериализация подключений (Connection)
class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'


# История хайлайтов
class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'


# Сериализация история игры (GameHistory)
class GameSerializer(serializers.ModelSerializer):
    highlight = HighlightSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = [
            'id',
            'game_time_start',
            'player_id_left',
            'player_id_right',
            'player_score_left',
            'player_score_right',
            'game_time',
            'game_name',
            'game_mode',
            'connection',
            'highlight'
        ]
