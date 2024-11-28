import pygame


class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (180, 150, 150)
        self.bg_image = pygame.image.load('images/background.jpg')

        # Настройки корабля
        self.ship_speed = 2.5

        # Настройки пришельцев
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Настройки снаряда
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 150, 75)
        self.bullets_allowed = 5
