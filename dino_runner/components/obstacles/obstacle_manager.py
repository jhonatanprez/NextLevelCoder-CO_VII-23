import pygame
import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, DRAGON_TYPE,FIRE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.dart import Dart

class ObstacleManager:

    POS_X = 300
    POS_Y = 300

    def __init__(self):
        self.cont = 0
        self.image_fire = FIRE
        self.fires = False
        self.bono = False
        self.rect = self.image_fire.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.has_obstacle = False
        self.obstacle = None
        self.obstacle_next = self.obstacle

    def update(self,game, user_input):
        if not self.has_obstacle:
            self.create_obstacle()
        self.has_obstacle = self.obstacle.update(game.game_speed)  
        if game.player.rect.colliderect (self.obstacle.rect):
            if game.player.type == SHIELD_TYPE:
                game.player.type = DEFAULT_TYPE
                self.has_obstacle = False
            else:
                pygame.time.delay(400)
                game.playing = False

        if game.player.type == DRAGON_TYPE:
            self.fires= True
            if user_input[pygame.K_LCTRL]:
                self.bono = True
                self.rect = self.image_fire.get_rect()
                self.rect.x = self.POS_X
                self.rect.y = self.POS_Y
                self.fires = self.obstacle.update(game.game_speed) 
                if self.image_fire.colliderect (self.obstacle.rect):
                    self.has_obstacle = False
                    self.bono = False
                    self.cont += 1
                    if self.cont == 3:
                        game.player.type = DEFAULT_TYPE
                    





    def create_obstacle(self):
        self.obstacle_next= [Dart(),Bird(),Cactus()]
        self.obstacle = random.choice(self.obstacle_next)
        self.has_obstacle = True

    def draw (self,screen ):
        if self.has_obstacle:
            self.obstacle.draw(screen)
        if self.fires:
            if self.bono:
                screen.blit(self.image_fire,self.rect)

