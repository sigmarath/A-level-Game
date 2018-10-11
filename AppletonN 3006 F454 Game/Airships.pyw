import pygame
import imp
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "Data"))

import var
import sidescroller


airship = pygame.image.load('data/sidescrollerAssets/enemies/norm1.png')
airship = pygame.transform.scale(airship, (207, 108))
if var.fullscreen == True:
    screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((900, 700))

var.run = True
pygame.init()

while True:
    x = 600
    y = 100

    count = 1
    screen.fill((0, 0, 0))
    for i in range(0, var.world):
        if y > 500:
            x -= 270
            y = 100
        screen.blit(airship, (x, y))
        y += 200
    pygame.display.update()
    while count < 20:
        count += 1
        for event in pygame.event.get():
            #for quitting pygame
            if event.type == pygame.QUIT: exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if var.fullscreen == True:
                        screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((900, 700))
                    var.fullscreen = not var.fullscreen
				

        pygame.time.Clock().tick(10)

    while var.level <= 5:
        imp.reload(sidescroller)
        var.level += 1

    var.world += 1
    var.level = 1

