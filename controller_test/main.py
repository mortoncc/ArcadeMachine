import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Controller Test")

pygame.display.update()

gameExit = False

lead_x = 300
lead_y = 300

white = (255, 255, 255)
red = (255, 0, 0)

joysticks = []
clock = pygame.time.Clock()

for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

while not gameExit:
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    
    if event.type == pygame.JOYAXISMOTION:
        print(joysticks[0].get_axis(0))
        if joysticks[0].get_axis(0) >= 0.5:    # Right
            lead_x += 10
        if joysticks[0].get_axis(0) <= -0.5:   # Left
            lead_x -= 10
        if joysticks[0].get_axis(0) > -0.5 and joysticks[0].get_axis(0) < 0.5:  # Up
            lead_y -= 10
        if joysticks[0].get_axis(0) > -0.5 and joysticks[0].get_axis(0) < 0.5:   # Down
            lead_y += 10
    
    gameDisplay.fill(red)
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, 20, 20])

    pygame.display.update()

pygame.quit()
quit()