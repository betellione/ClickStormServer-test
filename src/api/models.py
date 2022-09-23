from django.db import models

from django.db.models import Q


# Сессии игры
class Connection(models.Model):
    # Дата создания подключения
    date_create = models.DateTimeField(auto_now=True, verbose_name='Дата начала сессии')
    # ID клуба
    club_id = models.IntegerField(verbose_name='ID клуба')
    # ID устройства
    connection_id = models.IntegerField(verbose_name='ID устройства')
    # Ключи подключения
    key_connection = models.TextField(verbose_name='Ключи подключения')
    # ID текущего пользователя (left)
    id_left_user = models.IntegerField(blank=True, null=True, verbose_name='ID текущего пользователя (left)')
    # Имя текущего пользователя (left)
    name_left_user = models.TextField(blank=True, null=True, verbose_name='Имя текущего пользователя (left)')
    # ID текущего пользователя (right)
    id_right_user = models.IntegerField(blank=True, null=True, verbose_name='ID текущего пользователя (right)')
    # Имя текущего пользователя (right)
    name_right_user = models.TextField(blank=True, null=True, verbose_name='Имя текущего пользователя (right)')
    # Название клуба
    club_title = models.TextField(blank=True, null=True, verbose_name='Название клуба')
    # Тип девайса
    device_type = models.TextField(blank=True, null=True, verbose_name='Тип девайса')
    # Название девайса
    device_title = models.TextField(blank=True, null=True, verbose_name='Название девайса')

    # Получить сыгранные матчи
    def get_game_history(self):
        return Game.objects.filter(session=self)


# Результат сыгранных игр
class Game(models.Model):
    # Дата начал матча
    game_time_start = models.DateTimeField()

    # ID игрока лево
    player_id_left = models.IntegerField()
    # ID игрока право
    player_id_right = models.IntegerField()

    # Счет играка лево
    player_score_left = models.IntegerField(default=0)
    # Счет играка право
    player_score_right = models.IntegerField(default=0)

    # Время игры
    game_time = models.TimeField(blank=True, null=True)

    # Название игры
    game_name = models.TextField(blank=True, null=True)
    # Режим игры
    game_mode = models.TextField(blank=True, null=True)

    # Сессия игры
    connection = models.ForeignKey(Connection, related_name="games", on_delete=models.CASCADE)

    # Был ли конец игры
    is_end_game = models.BooleanField(default=False)

    # Получить победителя (None - ничия)
    def get_winner(self):
        if self.player_score_left > self.player_score_right:
            return self.player_score_left
        elif self.player_score_left < self.player_score_right:
            return self.player_score_right
        else:
            return None

    # Получить результат матча
    def get_result_game(self):
        return f'{self.player_score_left}:{self.player_score_right}'

    # Получить список ссылок на хайлайты
    def get_highlight(self):
        link_list = []

        for highlight in Highlight.objects.filter(game=self):
            link_list.append(highlight.link)

        return link_list


# История хайлайтов
class Highlight(models.Model):
    # Игры
    game = models.ForeignKey(Game, related_name="highlight", on_delete=models.CASCADE)
    # Ссылка на вк
    link = models.TextField()
