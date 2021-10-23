# I purposefully over-commented so that it would be easier for a beginner to understand
# exactly what each line is doing. If you know what you're doing then this file is not for you.

import pygame
# initializes pygame
pygame.init()

# creates display window that is 800 pixels by 800 pixels
gameDisplay = pygame.display.set_mode((800, 800))
# sets window caption (text in bar on far left)
pygame.display.set_caption("Controller Test")

# pushes the changes we made above through (actually displays them on the screen)
pygame.display.update()

# creates gameExit variable. this will be what we use to control whether the
# game will continue to run or not
gameExit = False

# starting x position is 300
lead_x = 300
# starting y position is 300
lead_y = 300

# creates variables for the colors "white" and "red" using their RGB values
white = (255, 255, 255)
red = (255, 0, 0)

# creates an array for our joysticks. this list will contain all the joysticks that will be used in the game
# for example, the arcade machine has 2 joysticks so there will be 2 items in the joystick list. the joystick
# on the left, and the joystick on the riht
joysticks = []

# creates the clock the game will use. this is so that we can set how quickly we want the game to run.
# For example, we can set it to run at 60 frames per second. If we left this out, it would run as quickly
# as the processor in the computer it's being ran on would allow.
clock = pygame.time.Clock()

# this goes through the "joysticks" list and initializes each joystick
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

# this is the MAIN GAME LOOP. while gameExit is false, we will continue playing game
while not gameExit:
    # i have set the game to run at 60 frames per second. this means that every second, 
    # this while loop will run 60 times.
    clock.tick(60)

    # every action we take causes an event. this for loop checks those events
    # to see if there is a QUIT event. if there is, we make gameExit (the variable
    # that controls our MAIN GAME LOOP and we set it to true so it stops)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    
    # Checks if the latest event is of type JOYAXISMOTION. If it is of type JOYAXISMOTION,
    # that means that a joystick has been moved
    if event.type == pygame.JOYAXISMOTION:
        # these if statements get the axis of the joystick's tilt and determine whether
        # it's moving left, right, up, or down and updates the coordinates of the rectangle accordingly.
        # essentially, if the axis is around 1 then we're moving right, if the axis is around -1 then we're moving left.
        # both movement upward and downward are defined as an axis of 0 which is causing me some trouble.
        # THIS IS CURRENTLY ONLY WORKING FOR LEFT/RIGHT MOVEMENT.
        if joysticks[0].get_axis(0) >= 0.5:    # Right
            lead_x += 10
        if joysticks[0].get_axis(0) <= -0.5:   # Left
            lead_x -= 10
        if joysticks[0].get_axis(0) > -0.5 and joysticks[0].get_axis(0) < 0.5:  # Up
            # our coordinate plane has x as increasing from left to right
            # and y increasing from top to bottom. this means that subtracting
            # from our y coordinate actually moves us upward, not downward.
            lead_y -= 10
        if joysticks[0].get_axis(0) > -0.5 and joysticks[0].get_axis(0) < 0.5:   # Down
            lead_y += 10
    
    # fill the entire display with red
    gameDisplay.fill(red)
    # draw our rectangle over the red in its designated position
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, 20, 20])
    # push the changes we made above to our window that's running the game
    pygame.display.update()

# quit everything once we're out of the main game loop
pygame.quit()
quit()