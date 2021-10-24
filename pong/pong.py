import sys
import pygame
import random
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

player_1 = pygame.Rect(25, 300, 35, 200)
player_2 = pygame.Rect(740, 300, 35, 200)
ball = pygame.Rect(400 - (35/2), 400 - (35/2), 35, 35)
white = (255, 255, 255)
black = (0, 0, 0)
motion_player_1 = [0, 0]
motion_player_2 = [0, 0]
motion_ball = [0, 0]

start_direction = random.randint(0, 2)

while True:

    screen.fill(black)

    pygame.draw.rect(screen, white, player_1)
    pygame.draw.rect(screen, white, player_2)
    pygame.draw.rect(screen, white, ball)

    if abs(motion_player_1[1]) < 0.1:
        motion_player_1[1] = 0
    player_1.y += motion_player_1[1] * 10

    if abs(motion_player_2[1]) < 0.1:
        motion_player_2[1] = 0
    player_2.y += motion_player_2[1] * 10

    for event in pygame.event.get():
        if (event.type == JOYAXISMOTION) and (event.axis == 0 or event.axis == 1):
            if event.axis < 2:
                motion_player_1[event.axis] = event.value
        if (event.type == JOYAXISMOTION) and (event.axis == 2 or event.axis == 3):
            if event.axis < 4:
                motion_player_2[event.axis - 2] = event.value
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)