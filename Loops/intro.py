#    mmm   mmmm  mmm     mmmm   mmmm   mmmm
#  m"   " #"   "   #    #    # "   "# m"  "m
#  #      "#mmm    #    "mmmm"   mmm" #  m #
#  #          "#   #    #   "#     "# #    #
#   "mmm" "mmm#" mm#mm  "#mmm" "mmm#"  #mm#

import pygame
from SimpleGUICS2Pygame import simplegui_lib_draw
from Classes.Objects import gameState1
#LOADING LIBRARIES

def introLoop(canvas):

    left, middle, right = pygame.mouse.get_pressed()

    if left:

        gameState1.introToMain()

    canvas.draw_text('welcome to the game Press anywhere to start', (150, 200), 30, "Magenta")

    simplegui_lib_draw.draw_rect(canvas, (250,250),
                                 (100,100), 1, 'Black', fill_color='Black')


def waitingLoop(canvas):
    canvas.draw_text('waiting for player 2', (150, 200), 30, "Magenta")

    simplegui_lib_draw.draw_rect(canvas, (250, 250),
                                 (100, 100), 1, 'Black', fill_color='Black')

