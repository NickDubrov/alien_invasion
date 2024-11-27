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
