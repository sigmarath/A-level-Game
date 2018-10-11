import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "Data"))
import var
import pygame
import random
import imp
import EngineRoom
import Cockpit

var.EngineRoomRun = True
var.CockpitRun = True
level = var.level
k = var.k
fullscreen = var.fullscreen
#setting the level

if var.run == True:
    pygame.init() 	#initiating pygame
    if fullscreen == True:
        screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((900, 700))

    sky = pygame.image.load('Data/sprites/sky/'+str(level)+'.png')
    sky = pygame.transform.scale(sky, (900, 700))
    fps = pygame.time.Clock()			#to allow theclock to tick

    #defining the arrays for the scrolling backgrounds
    islands = [[1], [1]]
    x = [[0], [0], [0]]
    back = False
    for i in range(1, ((level)*5)):
            back = not back
            islands[0].append(random.randint(1, 10))
            if back == True:
                    islands[1].append(random.randint(1, 5))
            for f in x:
                    f.append(f[i-1]+900)

    #defining the scrolling function
    def scroll():
            lenx = len(x)
            for i in range(0, lenx):
                    leni = len(x[i])
                    for f in range(0, leni):
                            x[i][f] -= (1/(i+1)*10)

    def foregroundblit():
            leni = len(islands[0])
            for i in range(0, leni):
                    foreground = pygame.image.load('Data/sidescrollerAssets/level'+str(level)+'/foreground/'+str(islands[0][i])+'.png')
                    foreground = pygame.transform.scale(foreground, (900, 900))
                    screen.blit(foreground, (x[0][i], 50))

    def backgroundblit():
            leni = len(islands[1])
            for i in range(0, leni):
                    background = pygame.image.load('Data/sidescrollerAssets/level'+str(level)+'/background/'+str(islands[1][i])+'.png')
                    background = pygame.transform.scale(background, (900, 900))
                    screen.blit(background, (x[1][i], 0))

    def skyblit():
            leni = len(x[2])
            for i in range(0, leni):
                    screen.blit(sky, (x[2][i], 0))

    def stats():
            heart = pygame.image.load('Data/sidescrollerAssets/heart.png')
            heart = pygame.transform.scale(heart, (24, 24))
            screen.blit(heart, (600, 10))
            engine = pygame.image.load('Data/sidescrollerAssets/gear.png')
            engine = pygame.transform.scale(engine, (24, 24))
            screen.blit(engine, (600, 45))
            #healthbar and engine bar backdrop
            pygame.draw.rect(screen, (200, 200, 200), (630, 10, 204, 24))
            pygame.draw.rect(screen, (200, 200, 200), (630, 45, 204, 24))
            #actual bars
            if health > 0:
                pygame.draw.rect(screen, (255, 0, 0), (632, 12, health*2, 20))
            if var.engineQual > 0:
                pygame.draw.rect(screen, (50, 80, 50), (632, 47, var.engineQual*2, 20))

    def draw():
            skyblit()
            backgroundblit()
            for i in boom:
                i.boom()
            boom.draw(screen)
            bullets.update()
            bullets.draw(screen)
            
            ships.draw(screen)
            ships.update()
            foregroundblit()
            stats()


    class player(pygame.sprite.Sprite):
            def __init__(self, x, y, imgs):
                    self.count = 4
                    pygame.sprite.Sprite.__init__(self)
                    self.imgs = imgs
                    self.pic = True
                    self.image = self.imgs[0]
                    self.x = x
                    self.y = y
                    self.position = (x, y)
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (self.x, self.y)

            def update(self):
                    self.count -= 1
                    if self.count <= 0:
                            self.pic = not self.pic
                            self.count = 4
                    if self.pic == True:
                            self.image = self.imgs[0]
                    else:
                            self.image = self.imgs[1]
                    self.rect = self.image.get_rect()
                    
                    key = pygame.key.get_pressed()
                    if key[pygame.K_w] and self.y > 20:
                            self.y -= 10
                    if key[pygame.K_a] and self.x > 20:
                            self.x -= 10
                    if key[pygame.K_s] and self.y < 500:
                            self.y += 10
                    if key[pygame.K_d] and self.x < 600:
                            self.x += 10

                    if self.x <= 20:
                            self.x += 10
                    self.rect.topleft = (self.x, self.y)

    class enemy(pygame.sprite.Sprite):
            def __init__(self, start, y, imgs):
                  pygame.sprite.Sprite.__init__(self)
                  self.count = 4
                  self.imgs = imgs
                  self.pic = True
                  self.start = int(start)
                  self.x = 950
                  self.y = int(y)
                  self.image = pygame.image.load(self.imgs[0])
                  self.rect = self.image.get_rect()
                  self.rect.topleft = (self.x, self.y)
                  self.tick = 1
                  
            def update(self):
                    self.x -= 15
                    self.count -= 1
                    if self.count <= 0:
                            self.pic = not self.pic
                            self.count = 4
                    if self.pic == True:
                            self.image = pygame.image.load(self.imgs[0])
                    else:
                            self.image = pygame.image.load(self.imgs[1])
                    self.image = pygame.transform.scale(self.image, (138, 72))
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (self.x, self.y)
                    for i in bullets:
                        if pygame.sprite.collide_rect(i, self):
                            bullets.remove(i)
                            ships.remove(self)
                            boom.add(self)
                            self.count = 2

            def boom(self):
                    self.count -= 1
                    if self.count <= 0:
                        self.tick += 1
                        self.count = 2
                        if self.tick == 8:
                            boom.remove(self)
                    self.x -= 15
                    self.image = pygame.image.load('Data/sprites/explosion/'+str(self.tick)+'.png')
                    self.image = pygame.transform.scale(self.image, (270, 270))
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (self.x - 70, self.y - 70)

    class bullet(pygame.sprite.Sprite):
            def __init__(self, x, y, img, direction):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.transform.scale(pygame.image.load(img), (50, 50))
                    self.direction = direction
                    if self.direction == False:
                            self.image = pygame.transform.flip(self.image, True, False)
                    self.x = x
                    self.y = y
                    self.position = (x, y)
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (self.x, self.y)
            def update(self):
                    if self.direction == True:
                            self.x += 50
                    else:
                            self.x -= 30
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (self.x, self.y)  
                    

    imgs = [pygame.transform.scale(pygame.image.load('Data/sidescrollerAssets/player1.png'), (150, 150))]
    imgs.append(pygame.transform.scale(pygame.image.load('Data/sidescrollerAssets/player2.png'), (150, 150)))

    xp = -40
    yp = 300

    enemy_positions = open('Data/sidescrollerassets/enemyinfo.txt').read().splitlines()

    #adding sprites
    player = player(xp, yp, imgs)

    #adding enemy sprites
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    boom = pygame.sprite.Group()


    if level > 3:
        rng = int(((level)*2)*10)
    else:
        rng = int(((level)**2)*10)
    for i in range(0, var.world):
        line = 1
        for l in range(0, rng):
            enemies.add(enemy(enemy_positions[line+1], enemy_positions[line+2], [enemy_positions[line+3], enemy_positions[line+4]]))
            line += 5


    ships = pygame.sprite.Group(player)

    bulletcount = 0
    finished = False
    dead = False
    health = 100
    run = True
    paused = False
    pausebanner = pygame.image.load('Data/sprites/paused.png')
    tutorialImg = pygame.image.load('Data/sidescrollerAssets/tutorial.png')
    tutorial = False
    K_code = False
    kpress = False

    while run == True: 
            pygame.display.set_caption('World: '+str(var.world)+'  Level: '+str(level))

            for event in pygame.event.get():
                #for quitting pygame
                if event.type == pygame.QUIT: exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        var.fullscreen = not var.fullscreen
                        if var.fullscreen == True:
                            screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((900, 700))
                        
                
                    if event.key == pygame.K_ESCAPE:
                        paused = True
                    if event.key == pygame.K_SLASH:
                        tutorial = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SLASH:
                        tutorial = False

            if finished == False and dead == False:
                while paused == True:
                    screen.fill((0, 0, 0))
                    skyblit()
                    backgroundblit()
                    screen.blit(pausebanner, (130, 50))
                    foregroundblit()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                paused = False
                                k = 0

                        key = pygame.key.get_pressed()
                        if event.type == pygame.KEYDOWN and kpress == False:
                            kpress = True
                            if key[pygame.K_UP]:
                                if k == 0 or k == 1:
                                    k += 1
                                else:
                                    k = 0

                            elif key[pygame.K_DOWN]:
                                if k == 2 or k == 3 :
                                    k += 1
                                else:
                                    k = 0
                            
                            elif key[pygame.K_LEFT]:
                                if k == 4 or k == 6:
                                    k += 1
                                else:
                                    k = 0
                            elif key[pygame.K_RIGHT]:
                                if k == 5 or k == 7:
                                    k += 1
                                else:
                                    k = 0
                            elif key[pygame.K_b]:
                                if k == 8:
                                    k += 1
                                else:
                                    k = 0
                            elif key[pygame.K_a]:
                                if k == 9:
                                    k += 1
                                else:
                                    k = 0
                            elif key[pygame.K_RETURN]:
                                if k == 10:
                                    print('konamai code unlocked')
                                    K_code = True
                                    health = 150
                                    engineQual = 150
                            else:
                                k = 0
                            print(k)

                        if event.type == pygame.KEYUP:
                            kpress = False

                    pygame.display.update()
                    fps.tick(60)



                screen.fill((0, 0, 0))
                if x[0][len(x[0])-1] > 0:
                        scroll()

                draw()
                for i in enemies:
                    if x[0][0] == -i.start:
                        ships.add(i)
                    elif i.x <= -200:
                        ships.remove(i)
                        enemies.remove(i)
                        health -= level**2 * 2
                if health <= 0:
                    dead = True
                    count = 0
                    boom_num = 1
                    boomx = player.x-70
                    boomy = player.y-70

                if x[0][0] == -(len(x[0])-1)*900:
                    finished = True
                    count = 3
                    missile = 1

                
                if tutorial == True:
                    screen.blit(tutorialImg, (0, 0))

                if x[0][0] == -300 and level == 1 and var.world == 1:
                    tutorial = True
                    screen.blit(tutorialImg, (0, 0))
                    pygame.display.update()
                    while tutorial == True:
                            for event in pygame.event.get():
                                #for quitting pygame
                                if event.type == pygame.QUIT: exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RETURN:
                                        tutorial = False

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and bulletcount <= 0:
                        bullets.add(bullet(player.x+75, player.y+70, 'Data/sidescrollerAssets/bullet.png', True))
                        if K_code == True:
                            bulletcount = 2
                        else:
                            bulletcount = 5


            elif finished == True: 
                bullets.update()
                player.x += 5
                ships.update()
                if missile < 8:
                    screen.fill((0, 0, 0))
                    skyblit()
                    backgroundblit()
                    ships.draw(screen)
                    missile_img = 'Data/sprites/missile/'+ str(missile) +'.png'
                    load_missile = pygame.image.load(missile_img)
                    load_missile = pygame.transform.scale(load_missile, (400, 400))
                    screen.blit(load_missile, (600, 250))
                    foregroundblit()
                    count -= 1
                    if count == 0:
                        count = 3
                        missile += 1
                else:
                    imp.reload(Cockpit)
                    var.CockpitRun = True
                    run = False

            elif dead == True:
                
                count += 1
                draw()
                player.y += (count*3)^2
                player.x += 25
                if var.engineQual <= 0:
                        ships.remove(player)
                        faliure_banner = pygame.image.load('Data/sprites/FAILED.png')
                        screen.blit(faliure_banner, (135, 50))
                        missile = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                        missile = pygame.transform.scale(missile, (270, 270))
                        screen.blit(missile, (boomx, boomy))
                        if count == 5:
                               boom_num += 1
                               count = 1
                        if boom_num == 8:
                                exit()
                elif player.y >= 800:
                    var.engineQual -= 20
                    imp.reload(EngineRoom)
                    for i in ships:
                            ships.remove(i)
                    ships.add(player)
                    var.EngineRoomRun = True
                    dead = False
                    player.x = xp
                    player.y = yp
                    health = 100




            bulletcount -= 1

            pygame.display.update()
            fps.tick(60)
