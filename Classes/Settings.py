'''
Class Id's:
1: Camera
2: particle
3: Player
4: Monster
'''
#FOR MULTIPLAYER MAKE SURE EACH PLAYER ID IS DIFFERENT, 1-4

#DEVELOPER OPTIONS
DEVELOPER_OPTIONS = False

#MAP
MAP_WIDTH = 10000
MAP_HEIGHT = 10000


#CANVAS
CANVAS_WIDTH = 1920
CANVAS_HEIGHT = 1080

#NETWORKING
CONFIG_TYPE = 'client'
CLIENT_IP = 'localhost'
LOGGING = True
LOGGING_LEVEL = 'low'

#CAMERA
CAM_MOVE_SENSITIVITY=60
CAM_ZOOM_SENSITIVITY=0.03
CAM_MIN_DIST=200
CAM_MAX_MOVE_DIST = 2000

#PARTICLE
PARTICLE_VELOCITY= 300
PARTICLE_RADIUS=20
PARTICLE_MAX_RANGE=2000
#SPRITE
SPRITE_FPS=1/20

#PLAYER
PLAYER_ID=1
PLAYER_RADIUS=40
PLAYER_MAX_VELOCITY=100
PLAYER_INITIAL_ANGLE=0
PLAYER_DIMENSIONS_X=50
PLAYER_DIMENSIONS_Y=100
PLAYER_INITIAL_VELOCITY_X=0
PLAYER_INITIAL_VELOCITY_Y=0
PLAYER_INITIAL_POSITION_X=2500
PLAYER_INITIAL_POSITION_Y=2500
PLAYER_SPRITE_FPS=10
PLAYER_SPRITE='ch_1'

#MAP
TREE_PROB_RANGE=100000