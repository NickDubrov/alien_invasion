import pygame

from game_functions import Functions
from button import Button
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Игра запускается в оконном режиме.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Создание кнопки Play.
        self.play_button = Button(self, "Play")

        # Создание экземпляров для хранения статистики и панели результатов.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Создание экземпляра корабля, группировка пришельцев и снарядов.
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Создание экземпляра для хранения игровых функций.
        self.functions = Functions(self)

        # Создание флота пришельцев.
        self.functions._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self.functions._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.functions._update_aliens()
                self.functions._update_bullets()

            self.functions._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
