from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird (Obstacle):

    STEP_INDEX = 0

    def __init__(self):
        image = BIRD[0] if self.STEP_INDEX < 5 else BIRD[1]
        self.STEP_INDEX +1
        super(). __init__(image)
        self.rect.y = 255
        
        