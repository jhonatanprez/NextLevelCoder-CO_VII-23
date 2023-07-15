import pygame

from pygame.sprite import Sprite  ##importamos sprite pygame
from dino_runner.utils.constants import(
    CLOUD,
    RUNNING,
    DUCKING,
    JUMPING
)

class Dinosaur:

    POS_X = 80
    POS_Y = 300
    DUCK_POS_Y = 340
    JUMP_VEL = 8.5
    X_CLOUND = 1000
    Y_CLOUND = 200
    

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.runnig = True
        self.ducking = False
        self.jumping = False
        self.jumping_velocity = self.JUMP_VEL
        self.cloud_speed = 10

    def update(self, user_input):
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.runnig:
            self.run()
        if (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.jumping:
            self.runnig = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP]:
            self.runnig = False
            self.ducking = False
            self.jumping = True
        elif not self.jumping and not self.ducking:
            self.runnig = True
            self.ducking = False
            self.jumping = False

        if self.step_index >= 10:
            self.step_index = 0
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        self.background()

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1

    def jump (self):
        self.image = JUMPING
        if self.jumping:
            self.rect.y -= self.jumping_velocity*4
            self.jumping_velocity -= 0.8
        if self.jumping_velocity < -self.JUMP_VEL:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_VEL
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUCK_POS_Y
        self.step_index += 1

    def background(self):
        self.image = CLOUD
        self.rect = self.image.get_re
        self.rect.x -= self.cloud_speed
        if self.rect.x <= 0:
            self.rect.x = self.X_CLOUND    
 