# Engine room #
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "Data"))
import var
import pygame
import random

level = var.level
world = var.world
fullscreen = var.fullscreen

if var.EngineRoomRun == True:
    #sprites for valve_s
    class valve(pygame.sprite.Sprite):
            def __init__(self, condition, worth):
                    pygame.sprite.Sprite.__init__(self)
                    #defining images for turning valves
                    self.image_stat = pygame.image.load('Data/sprites/valve_1.png')
                    self.image_turn = pygame.image.load('Data/sprites/valve_2.png')
                    #setting worth and condition
                    self.worth = worth
                    self.condition = condition
                    self.image = self.image_stat
            def turn(self, position): #when the buton is pressed, the valve will turn
                    self.condition = not self.condition
                    #setting image worth of switch
                    if self.condition == 1:
                            self.image = self.image_stat
                    else:
                            self.image = self.image_turn
                    if self.condition == True:
                            self.current_worth = self.worth
                    else:
                            self.current_worth = 0
                    self.rect = self.image_stat.get_rect()
                    self.rect.topleft = position
    #defining the sprites for the target numbers
    class Number(pygame.sprite.Sprite):
            def __init__(self, pos, num):
                    pygame.sprite.Sprite.__init__(self)
                    #loads relevant number image
                    self.num = num
                    self.image = pygame.image.load('Data/sprites/hanging_numbers/'+str(self.num)+'.png')
                    self.rect = self.image.get_rect()
                    self.rect.topleft = pos 	#position

    #funcntion for blitting everything
    def blit_all():
        global smoke_count
        global smoke_num
        global smoke_size
        global chug
        global count
        screen.blit(sky, (0, 0))
        if time <= 0: smoke_size = 3
        if victory == True: smoke_size = 1
        smoke = pygame.image.load('Data/sprites/smoke/'+str(smoke_size)+'_'+str(smoke_num)+'.png')
        smoke = pygame.transform.scale(smoke, (400, 400))
        screen.blit(smoke, (450, 50))
        smoke_count += 1
        if smoke_count == 16:
                if smoke_num == 3:
                    smoke_num = 1
                else:
                    smoke_num += 1
                smoke_count = 0
        if count <= 0:
                count += count_s
                smoke_size += 1
                if victory == True:
                    count = 1000

        screen.blit(deck, (0, 0))
        if chug < 1:
                screen.blit(pipes, (60, 46))
                screen.blit(engine, (-10, 250))
        elif chug < 6:
                screen.blit(pipes, (60, 47))
                screen.blit(engine, (-11, 250))
        elif chug < 9:
                screen.blit(pipes, (60, 48))
                screen.blit(engine, (-12, 250))
        elif chug < 12:
                screen.blit(pipes, (60, 47))
                screen.blit(engine, (-11, 250))
        chug += 1
        if chug == 12: chug = 0
        #the plaques
        if world == 1:
            screen.blit(pygame.image.load('Data/sprites/plaque/1.png'), (60, 205))
            screen.blit(pygame.image.load('Data/sprites/plaque/2.png'), (100, 205))
            screen.blit(pygame.image.load('Data/sprites/plaque/3.png'), (160, 205))
            screen.blit(pygame.image.load('Data/sprites/plaque/4.png'), (220, 205))
            screen.blit(pygame.image.load('Data/sprites/plaque/5.png'), (280, 205))
            screen.blit(pygame.image.load('Data/sprites/plaque/6.png'), (320, 205))
            screen.blit(pygame.image.load('Data/sprites/plaque/7.png'), (360, 205))
            screen.blit(pygame.image.load('Data/sprites/plaque/8.png'), (400, 205))
        #blitting the lights
        x = 42
        lightcount = 1
        if valve_1.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (82, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (82, 120))
        if valve_2.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (122, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (122, 120))
        if valve_3.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (182, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (182, 120))
        if valve_4.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (242, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (242, 120))
        if valve_5.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (302, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (302, 120))
        if valve_6.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (342, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (342, 120))
        if valve_7.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (382, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (382, 120))
        if valve_8.condition == True:
                screen.blit(pygame.image.load('Data/sprites/light_on.png'), (422, 120))
        else:
                screen.blit(pygame.image.load('Data/sprites/light_off.png'), (422, 120))
        if altcount < 9:
            alt = pygame.image.load('Data/sprites/altimeter/'+str(altcount)+'.png')
            screen.blit(alt, (400, 280))
                        

        #the sprites
        sprites.draw(screen)


    #starting the game
    pygame.init()
    #defining background ready for blitting
    if fullscreen == True:
        screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((900, 700))
    deck = pygame.image.load('Data/sprites/deck.png')
    deck = pygame.transform.scale(deck, (900, 700))
    sky = pygame.image.load('Data/sprites/sky/'+str(level)+'.png')
    sky = pygame.transform.scale(sky, (910,500))
    pipes = pygame.image.load('Data/sprites/pipes.png')
    pipes = pygame.transform.scale(pipes, (500, 600))
    engine = pygame.image.load('Data/sprites/engine.png')
    engine = pygame.transform.scale(engine, (550, 600))

    fps = pygame.time.Clock()		#to allow the clock to tick
    time = 500*(10/level)/world			#hoe long they have til crash
    target = random.randint(0, 255)	#random target number
    #splitting the target into 3
    if len(str(target)) == 1:
            digit_1 = 0 
            digit_2 = 0
            digit_3 = int(str(target)[0])
    elif len(str(target)) == 2:
            digit_1 = 0
            digit_2 = int(str(target)[0])
            digit_3 = int(str(target)[1])
    else:
            digit_1 = int(str(target)[0])
            digit_2 = int(str(target)[1])
            digit_3 = int(str(target)[2])
    #putting targets into sprites
    Number_1 = Number((0, 0), digit_1)
    Number_2 = Number((70, 0), digit_2)
    Number_3 = Number((140, 0), digit_3)
    #making the valve sprites
    valve_1 = valve(random.choice((True, False)), 128)
    valve_1.turn((60, 150))
    valve_2 = valve(random.choice((True, False)), 64)
    valve_2.turn((100, 150))
    valve_3 = valve(random.choice((True, False)), 32)
    valve_3.turn((160, 150))
    valve_4 = valve(random.choice((True, False)), 16)
    valve_4.turn((220, 150))
    valve_5 = valve(random.choice((True, False)), 8)
    valve_5.turn((280, 150))
    valve_6 = valve(random.choice((True, False)), 4)
    valve_6.turn((320, 150))
    valve_7 = valve(random.choice((True, False)), 2)
    valve_7.turn((360, 150))
    valve_8 = valve(random.choice((True, False)), 1)
    valve_8.turn((400, 150))

    #grouping the sprites
    valves = pygame.sprite.Group(valve_8, valve_7, valve_6, valve_5, valve_4, valve_3, valve_2, valve_1)
    numbers = pygame.sprite.Group(Number_1, Number_2, Number_3)
    sprites = pygame.sprite.Group(valves, numbers)
    #initialising variables for use in loop
    count_s = time/3 +10			#used for smoke counting
    count = count_s	
    alttime = time/8
    alttemp = alttime
    altcount = 1		
    failed = victory = False
    smoke_count = 1 				#for moving the smoke on
    smoke_num = 1
    smoke_size = 1
    smoke_tick = 1
    chug = 1
    caption = True				#used for caption of window
    caption_count = time/30
    #used for the tutorial
    Tutorial = False
    valve_turns = [False, False, False, False, False, False, False, False]
    Turn_count = 0

    #initialising faliure conditions
    count_boom = []
    position_boom = []
    size_boom = []
    for x in range(0, 10):
            count_boom.append(random.randint(-15, 1))
            position_boom.append((random.randint(-200, 500), random.randint(-200, 400)))
            size_boom.append(random.randint(400, 700))
            boom_tick = 1



    while var.EngineRoomRun == True:

            screen.fill((255, 255, 255))
            value = valve_1.current_worth + valve_2.current_worth + valve_3.current_worth + valve_4.current_worth + valve_5.current_worth + valve_6.current_worth + valve_7.current_worth + valve_8.current_worth

            for event in pygame.event.get():
                    if event.type == pygame.QUIT: exit()
                    if failed == False and victory == False:
                           if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_1:
                                        if var.fullscreen == True:
                                            screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
                                        else:
                                            screen = pygame.display.set_mode((900, 700))
                                        var.fullscreen = not var.fullscreen
                                    if event.key == pygame.K_a:
                                            valve_1.turn((60, 150))
                                    if event.key == pygame.K_s:
                                            valve_2.turn((100, 150))
                                    if event.key == pygame.K_d:
                                            valve_3.turn((160, 150))
                                    if event.key == pygame.K_f:
                                            valve_4.turn((220, 150))
                                    if event.key == pygame.K_g:
                                            valve_5.turn((280, 150))
                                    if event.key == pygame.K_h:
                                            valve_6.turn((320, 150))
                                    if event.key == pygame.K_j:
                                            valve_7.turn((360, 150))
                                    if event.key == pygame.K_k:
                                            valve_8.turn((400, 150))
                                    if event.key == pygame.K_RETURN:
                                            if value == target:
                                                    print('correct')
                                                    victory = True
                                                    count = 20
                                            else:
                                                    print('incorrect')
                                                    count -= 50*level
                                                    alttemp -= 50*level
                                                    time -= 50*level

            if failed == False and victory == False:
                    blit_all()
                    count -= 1
                    time -= 1
                    if caption_count <= 0:
                            caption = not caption
                            caption_count = time/30
                    if caption == True:
                            pygame.display.set_caption('[WARNING: LOSING ALTITUDE]')
                    else:
                            pygame.display.set_caption('....................................................') 
                    caption_count -= 1
                    if time <= 0:
                            print('time up')
                            failed = True
                            count = 0


                    alttemp -= 1
                    if alttemp <= 0:
                        alttemp = alttime
                        altcount += 1
                    
            #when they win the game
            if victory == True:
                    if count != 1000:
                         count -= 1
                    blit_all()
                    victory_banner = pygame.image.load('Data/sprites/VICTORY.png')
                    screen.blit(victory_banner, (75, 300))
                    if altcount > 1:
                        altcount -= 1
                    else:
                        var.EngineRoomRun = False
            if failed == True:
                blit_all()
                                #all small random explosions
                for num in range(0, 10):
                    #making sure they don't overlap the large explosion
                    if count_boom[num] < 9 and count_boom[num] > 0:
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(count_boom[num])+'.png')
                            explosion = pygame.transform.scale(explosion, (size_boom[num], size_boom[num]))
                            screen.blit(explosion, position_boom[num])
                    elif count_boom[num] > 9:
                            count_boom[num] = random.randint(-5, 0)
                            position_boom[num] = (random.randint(-200, 500), random.randint(-200, 400))
                            size_boom[num]=(random.randint(400, 700))
                    count_boom[num] += 1
                boom_tick += 1
                print(boom_tick)
                if boom_tick >= 20:          #ends the game after a cetain amount of time
                    exit()
                count += 1
                faliure_banner = pygame.image.load('Data/sprites/FAILED.png')
                screen.blit(faliure_banner, (135, 50))

            pygame.display.update()
            fps.tick(60)

