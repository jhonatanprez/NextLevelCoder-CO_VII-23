import pygame
import random

from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.dragon import Dragon


class PowerUpManager:

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = 100
        self.next_powerup = self.powerup

    def update(self, game):
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
            self.new_next_powerup_show = random.randint(500,1000)
            self.next_powerup_show += self.new_next_powerup_show
        if self.has_powerup:
            self.has_powerup = self.powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.powerup.rect):
                self.new_next_powerup_show = random.randint(500,1000)
                self.next_powerup_show += self.new_next_powerup_show
                self.has_powerup = False
                game.player.type = self.powerup.type

    def create_powerup(self):
        self.next_powerup = [Shield(), Dragon()]
        self.powerup = random.choice(self.next_powerup)
        self.has_powerup = True

    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)