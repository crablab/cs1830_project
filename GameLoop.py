print("""\
   mmm   mmmm  mmm     mmmm   mmmm   mmmm
 m"   " #"   "   #    #    # "   "# m"  "m
 #      "#mmm    #    "mmmm"   mmm" #  m #
 #          "#   #    #   "#     "# #    #
  "mmm" "mmm#" mm#mm  "#mmm" "mmm#"  #mm#
""")

import sys, configparser
from SimpleGUICS2Pygame import simplegui_lib_fps
from SimpleGUICS2Pygame import simpleguics2pygame

# LOADING SETTINGS
config = configparser.ConfigParser()
# Open file as writeable
config.read_file(open('Classes/config'))



# LOAD INTERNAL CLASSES
from Handlers.KeyHandler import keydown, keyup
from Handlers.ClickHandler import checkClick
from Loading.Objects import *

# -----START----GAME----CLOCK
fps = simplegui_lib_fps.FPS()
fps.start()


# --------------GAME-----LOOP-------------------
def draw(canvas):
    block.update()
    block.draw(canvas,cam)
    pass
# ========== GAME LOOPS NON MAIN =====================


# ========================== STATS DISPLAY ==============================================================


##
## Init
##
frame = simpleguics2pygame.create_frame('Game', int(config['CANVAS']['CANVAS_WIDTH']),
                                        int(config['CANVAS']['CANVAS_HEIGHT']))
frame.set_canvas_background('Black')

remote = frame.add_label('Remote Addr: ' + config['NETWORKING']['client_ip'])

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
