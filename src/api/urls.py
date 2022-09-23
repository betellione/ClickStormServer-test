from django.urls import path, re_path

from .views import *

urlpatterns = [
    # Список трансляций
    # Получить/создать
    path('connection_list', ConnectionAPIList.as_view()),
    # Определенная трансляция
    # Получить/изменить/удалить
    path('connection/<int:pk>', ConnectionAPI.as_view()),

    # Список игр
    path('game_list', GameAPIList.as_view()),
    # Определенная игры
    # Получить/изменить/удалить
    path('game/<int:pk>', GameAPI.as_view()),

    # Создать хайлайт
    path('highlight_list', HighlightAPIList.as_view())
]
