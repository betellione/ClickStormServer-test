from rest_framework import generics
from django.http import HttpResponse

from .serializer import *

import threading


# Получаем список подключений
# Создаем новое подключение
class ConnectionAPIList(generics.ListCreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


# Получаем информацию по подключению
# Редактируем информацию по подключению
# Удалить подключение
class ConnectionAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


# Получить список игр по id подключения
class GameAPIList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# Получаем информацию по подключению
# Редактируем информацию по подключению
# Удалить подключение
class GameAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# Получить игру по id
# Получить игры по id пользователя
class HighlightAPIList(generics.ListCreateAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
