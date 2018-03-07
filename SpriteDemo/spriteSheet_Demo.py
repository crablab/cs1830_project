import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from spriteSheetTemplate import *

class SpriteSheetDemo(SpriteSheetTemplate):
    def __init__(self):
        self.image = simplegui._load_local_image('guy.png')

        #Sprite(pos_middle, width, height):
        self.name_to_sprite_list = {
            'player_down'   :Sprite((32,32), 64, 64),
            'player_up'     :Sprite((96,32), 64, 64),
            'player_left'   :Sprite((160,32), 64, 64),
            'player_right'  :Sprite((224,32), 64, 64)
            }
