from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import DRAGON, DRAGON_TYPE


class Dragon(PowerUp):
    def __init__(self):
        selected_image = DRAGON
        super().__init__(selected_image)
        self.type = DRAGON_TYPE