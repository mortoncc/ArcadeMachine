import sys

import pygame

from pygame.locals import *
# initializes pygame
pygame.init()
# sets window text (top left corner text)
pygame.display.set_caption('game base')
# creates screen of size 500 pixels by 500 pixels
screen = pygame.display.set_mode((500, 500), 0, 32)
# creates clock for the game that determines speed at which it runs
clock = pygame.time.Clock()

# initialize pygame.joystick
pygame.joystick.init()
# create an array holding all joysticks
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

# create a square at (50, 50) with width and height of 50 pixels
my_square = pygame.Rect(50, 50, 50, 50)
# set square color to 0 (red)
my_square_color = 0
# creates list of colors (red, blue, green)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
# creates a list for motion [horizontal, vertical]
motion = [0, 0]

while True:

    # fill the screen with black
    screen.fill((0, 0, 0))

    # draw a black rectangle on the screen
    pygame.draw.rect(screen, colors[my_square_color], my_square)
    # sets a buffer for joystick so it's not too sensitive
    if abs(motion[0]) < 0.1:
        motion[0] = 0
    if abs(motion[1]) < 0.1:
        motion[1] = 0
    # adjusts motion of square according to changes in motion list
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10

    # checks all events that are occurring
    for event in pygame.event.get():
        # if a button is pressed on the joystick, change the color of the square
        if event.type == JOYBUTTONDOWN:
            print(event)
            if event.button == 0:
                my_square_color = (my_square_color + 1) % len(colors)
        # if the joystick is moved, set either horizontal or vertical movement to value of movement (based on tilt of joystick)
        if event.type == JOYAXISMOTION:
            print(event)
            if event.axis < 2:
                motion[event.axis] = event.value
        # if there was a quit event, quit the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    # all the changes above were only behind the scenes. this updates all changes to window that game is running in
    pygame.display.update()
    # set the game to run at 60 fps
    clock.tick(60)