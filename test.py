# Demonstration of a magnifier on a map

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simpleguics2pygame.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)


# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image,
                      [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT],
                      [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])

    # Draw magnifier
    map_center = [MAP_WIDTH // 2, MAP_HEIGHT // 2]
    map_rectangle = [MAP_WIDTH, MAP_HEIGHT]
    mag_center = mag_pos

    mag_rectangle = mag_pos
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)
    print("Image Size: " + str(map_rectangle))
    print("center: " + str(map_center))
    print("canvas Coords: " + str(mag_center))
    print("Size on Canvas: " + str(mag_rectangle))

# Create frame for scaled map
frame = simpleguics2pygame.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# Start frame
frame.start()
