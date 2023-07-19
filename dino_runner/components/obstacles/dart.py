import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import DART

class Dart (Obstacle):
    def __init__(self):
        selected_image = DART
        super().__init__(selected_image)
        self.rect.y = 0

    def update(self, game_speed):
        self.rect.y += 6
        return super().update(game_speed)
