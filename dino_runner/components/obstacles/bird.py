from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird (Obstacle):

    STEP_INDEX = 0

    def __init__(self):
        self.step_index = self.STEP_INDEX
        self.image = BIRD[0]
        super(). __init__(self.image)


        

    def update(self, game_speed):
        self.image = BIRD [0] if self.step_index < 5 else BIRD[1]
        if self.step_index >= 10:
            self.step_index = self.STEP_INDEX
        self.step_index +=1
        self.rect.y = 250
        return super().update(game_speed)
        


        


        
        
        
        