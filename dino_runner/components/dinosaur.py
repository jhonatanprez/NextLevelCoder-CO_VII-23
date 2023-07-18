import pygame

from pygame.sprite import Sprite  ##importamos sprite pygame
from dino_runner.utils.constants import(
    CLOUD,
    RUNNING,
    DUCKING,
    JUMPING,
    PLANT
)

class Dinosaur:

    POS_X = 80
    POS_Y = 300
    DUCK_POS_Y = 340
    JUMP_VEL = 8.5
    X_CLOUND = 1100
    Y_CLOUND = 40
    PLANT_X = 1320
    PLANT_Y = 390
    

    def __init__(self):
        self.image_plant = PLANT
        self.image_cloud = CLOUD
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.runnig = True
        self.ducking = False
        self.jumping = False
        self.jumping_velocity = self.JUMP_VEL
        self.cloud_speed = 7
        self.pos_x_cloud = self.X_CLOUND
        self.pos_y_cloud = self.Y_CLOUND
        self.pos_x_plant = self.PLANT_X
        self.pos_y_plant = self.PLANT_Y


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
        elif not self.jumping:
            self.runnig = True
            self.ducking = False
            self.jumping = False

        if self.step_index >= 10:
            self.step_index = 0
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        screen.blit(self.image_plant,[self.pos_x_plant , self.pos_y_plant])
        self.pos_x_plant -= self.cloud_speed
        if self.pos_x_plant < -150:
            self.pos_x_plant = self.PLANT_X
        screen.blit(self.image_cloud,[self.pos_x_cloud , self.pos_y_cloud])
        self.pos_x_cloud -= self.cloud_speed
        if self.pos_x_cloud <= -60:
            self.pos_x_cloud = self.X_CLOUND

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

