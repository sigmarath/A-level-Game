# Cockpit #
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "Data"))
import var
import pygame
import random

level = var.level
world = var.world

if var.CockpitRun == True:
    #sprites for switches
    class switch(pygame.sprite.Sprite):
    	def __init__(self, img_on, img_off, condition, worth):
    		pygame.sprite.Sprite.__init__(self)
    		#defining images on and off to easily call later
    		self.image_on = img_on
    		self.image_off  = img_off
    		#setting the worth for that sprite and condition and position
    		self.worth = worth
    		self.condition = condition
    	def flick(self, position): 	#whenever the button is pressed to flick tswitchhe 
    		self.condition = not self.condition
    		#setting image and worth of switch
    		if self.condition == True:
    			self.image = pygame.image.load(self.image_on)
    			self.current_worth = self.worth
    		else:
    			self.image = pygame.image.load(self.image_off)
    			self.current_worth = 0
    		self.rect = self.image.get_rect()
    		self.rect.topleft = position
    #defining the sprites for nixies
    class nixie(pygame.sprite.Sprite):
    	def __init__(self, pos, num):
    		pygame.sprite.Sprite.__init__(self)
    		#loads relevant number image
    		self.num = num
    		for x in range(10):
    			if x == self.num:
    				self.image = pygame.image.load('Data/sprites/nixie/nixie_'+str(x)+'.png')
    		self.rect = self.image.get_rect()
    		self.rect.topleft = pos 		#position
    	

    #starting the game
    pygame.init()
    #defining backgrounds ready for blitting
    if var.fullscreen == True:
        screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((900, 700))
    background = pygame.image.load('Data/sprites/cockpit.png')
    sky = pygame.image.load('Data/sprites/sky/'+str(level)+'.png')
    sky = pygame.transform.scale(sky, (910, 300))

    fps = pygame.time.Clock()			#to allow theclock to tick
    time = 500*(10/level)/world				#how long they have to diffuse the bomb
    target = random.randint(0, 255)		#random target number to reach with switches
    #splitting the target into 3 and putting into sprites
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
    #putting target into sprites
    nixie_1 = nixie((720, 400), digit_1)
    nixie_2 = nixie((745, 400), digit_2)
    nixie_3 = nixie((770, 400), digit_3)
    #flippers
    flipper_1 = flipper_2 = flipper_3 = pygame.image.load('Data/sprites/flipper/None.png')
    flipping = True
    #button
    button = pygame.image.load('Data/sprites/button_up.png')
    #making the 8 switch sprites
    switch_1 = switch( 'Data/sprites/switches/switch-1-on.png', 'Data/sprites/switches/switch-1-off.png', random.choice((True, False)), 128)
    switch_1.flick((35, 400))
    switch_2 = switch( 'Data/sprites/switches/switch-2-on.png', 'Data/sprites/switches/switch-2-off.png', random.choice((True, False)), 64)
    switch_2.flick((105, 400))
    switch_3 = switch( 'Data/sprites/switches/switch-3-on.png', 'Data/sprites/switches/switch-3-off.png', random.choice((True, False)), 32)
    switch_3.flick((175, 400))
    switch_4 = switch( 'Data/sprites/switches/switch-4-on.png', 'Data/sprites/switches/switch-4-off.png', random.choice((True, False)), 16)
    switch_4.flick((245, 400))
    switch_5 = switch( 'Data/sprites/switches/switch-5-on.png', 'Data/sprites/switches/switch-5-off.png', random.choice((True, False)), 8)
    switch_5.flick((321, 400))
    switch_6 = switch( 'Data/sprites/switches/switch-6-on.png', 'Data/sprites/switches/switch-6-off.png', random.choice((True, False)), 4)
    switch_6.flick((400, 400))
    switch_7 = switch( 'Data/sprites/switches/switch-7-on.png', 'Data/sprites/switches/switch-7-off.png', random.choice((True, False)), 2)
    switch_7.flick((470, 400))
    switch_8 = switch( 'Data/sprites/switches/switch-8-on.png', 'Data/sprites/switches/switch-8-off.png', random.choice((True, False)), 1)
    switch_8.flick((540, 400))

    #grouping sprites
    switches = pygame.sprite.Group(switch_8, switch_7, switch_6,switch_5, switch_4, switch_3, switch_2, switch_1)
    nixies = pygame.sprite.Group(nixie_1, nixie_2, nixie_3)
    sprites = pygame.sprite.Group(switches, nixies)
    #various variabled for use during loop
    get_value = False		#for when enter is pressed
    count_s = time/21		#to determine the length of each missile frame
    count = count_s			#when it = 0, it resets and the missile moves on a frame
    missile = 1 			#which missile frame it's on
    failed = victory = False	#have they succeeded or failed yet? 
    boom_num = 1 			#explosion frame number
    skycount = 0			#used for sky movement
    caption = True                  #used for flipping the caption
    caption_count = time/30
    #used for the tutorial
    Tutorial = False
    tutorial_cockpit = pygame.image.load('Data/sprites/tutorial_cockpit.png')
    #initialising faliure conditions
    count_boom = []
    position_boom = []
    size_boom = []
    for x in range(0, 10):
            count_boom.append(random.randint(-15, 1))
            position_boom.append((random.randint(0, 900), random.randint(0, 700)))
            size_boom.append(random.randint(75, 300))
            boom_tick = 1
    #function for blitting everything to the screen
    def blit_all():
            screen.blit(background, (0, 0)) #blits the cockpit
            global button
            button = pygame.transform.scale(button, (150, 150))
            screen.blit(button, (190, 485))
            #flipper blitting 
            screen.blit(flipper_1, (480, 500))
            screen.blit(flipper_2, (550, 500))
            screen.blit(flipper_3, (620, 500))

            #adding plaques
            if world == 1:
                    plax = 35
                    for num in range(1,9):
                            screen.blit(pygame.image.load('Data/sprites/plaque/'+str(num)+'.png'), (plax, 335))
                            plax += 72
            sprites.draw(screen) #draws ALL sprites
            #overlays Tutorial
            if Tutorial == True or level == 1 and time > 4500:
                    screen.blit(tutorial_cockpit, (0, 0))
    #event loop
    while var.CockpitRun == True:
            screen.fill((255, 255, 255))	#fills the screen with black
    	
            #moves sky back and forth
            if skycount < 30:
                    screen.blit(sky, (-5, 10))
            elif skycount < 60:
                    screen.blit(sky, (-2, 10))
            elif skycount < 90:
                    screen.blit(sky, (0, 10))
            elif skycount < 120:
                    screen.blit(sky, (-2, 10))
            skycount += 1
            if skycount == 120:	#resets sky animation
                    skycount = 0
            value = switch_1.current_worth + switch_2.current_worth + switch_3.current_worth + switch_4.current_worth + switch_5.current_worth + switch_6.current_worth + switch_7.current_worth + switch_8.current_worth
    	#checking all events
            for event in pygame.event.get():
    		#for quitting pygame
                    if event.type == pygame.QUIT: exit()
                    if failed == False and victory == False:
    		#run switch.flick to flick the switch when key pressed
                            if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_1:
                                        if var.fullscreen == True:
                                            screen = pygame.display.set_mode((900, 700), pygame.FULLSCREEN)
                                        else:
                                            screen = pygame.display.set_mode((900, 700))
                                        var.fullscreen = not var.fullscreen
                                    if event.key == pygame.K_a:
                                            switch_1.flick((35, 400))
                                    if event.key == pygame.K_s:
                                            switch_2.flick((105, 400))
                                    if event.key == pygame.K_d:
                                            switch_3.flick((175, 400))
                                    if event.key == pygame.K_f:
                                            switch_4.flick((245, 400))
                                    if event.key == pygame.K_g:
                                            switch_5.flick((321, 400))
                                    if event.key == pygame.K_h:
                                            switch_6.flick((400, 400))
                                    if event.key == pygame.K_j:
                                            switch_7.flick((470, 400))
                                    if event.key == pygame.K_k:
                                            switch_8.flick((540, 400))
                                    if event.key == pygame.K_SLASH:
                                            Tutorial = True
                                    if event.key == pygame.K_SPACE:
                                            get_value = True
                                            flip_count = 1
                                            value_temp = value
                                    if event.key == pygame.K_RETURN:
                                            button = pygame.image.load('Data/sprites/button_down.png')
                                            if value == target:
                                                    victory = True
                                                    count = 0
                                            else:
                                                    count -= 50*level
                                                    time -= 50*level
                            elif event.type == pygame.KEYUP:
                                    if event.key == pygame.K_RETURN:
                                            button = pygame.image.load('Data/sprites/button_up.png')
                                    if event.key == pygame.K_SLASH:
                                            Tutorial = False
            if failed == False and victory == False:        #main game loop
                    blit_all()
                    #moving on missile animation
                    if count <= 0:
                            count += count_s
                            missile += 1
                    #adding the timer and victory and faliure connditions
                    time -= 1
                    #flipping the flippers when space is pressed
                    if get_value == True:
                            if len(str(value_temp)) == 1:
                                flip_num_1 = '0'
                                flip_num_2 = '0' 
                                flip_num_3 = str(value_temp)[0]
                            elif len(str(value_temp)) == 2:
                                flip_num_1 = '0'
                                flip_num_2 = str(value_temp)[0]
                                flip_num_3 = str(value_temp)[1]
                            else:
                                flip_num_1 = str(value_temp)[0]
                                flip_num_2 = str(value_temp)[1]
                                flip_num_3 = str(value_temp)[2] 
                            if flip_count < (10*level)*world:
                                flipper_1 = pygame.image.load('Data/sprites/flipper/'+str(flipping)+'.png')
                            else:
                                flipper_1 = pygame.image.load('Data/sprites/flipper/'+flip_num_1+'.png')
                            if flip_count < (20*level)*world:
                                flipper_2 = pygame.image.load('Data/sprites/flipper/'+str(flipping)+'.png')
                            else:
                                flipper_2 = pygame.image.load('Data/sprites/flipper/'+flip_num_2+'.png')
                            if flip_count < (30*level)*world:
                                flipper_3 = pygame.image.load('Data/sprites/flipper/'+str(flipping)+'.png')
                            else:
                                flipper_3 = pygame.image.load('Data/sprites/flipper/'+flip_num_3+'.png')
                                get_value = False
                                flip_count = 0
                            flip_count += 1
                            flipping = not flipping
                    #flipping the caption to blink
                    if caption_count <= 0:
                            caption = not caption
                            caption_count = time/30         #slowly gets faster as missile nears
                    if caption == True:
                            pygame.display.set_caption('[WARNING: INCOMING MISSILE]')
                    else:
                            pygame.display.set_caption('....................................................')
                    caption_count -= 1
                    if time <= 0:           #running out of time
                            failed = True
                            count = 0
                    load_missile = pygame.image.load('Data/sprites/missile/'+ str(missile) +'.png')      #loading the missile
                    screen.blit(load_missile, (350, 100))
                    count -= 1
            #when they win the game
            if victory == True:
                    count += 1
                    if missile < 13:
                        if boom_num < 3:
                            screen.blit(load_missile, (350, 100))
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                            screen.blit(explosion, (400, 230 - missile*8))
                        elif boom_num < 9:
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                            screen.blit(explosion, (400, 230 - missile*8))
                    elif missile < 18:
                        if boom_num < 3:
                            screen.blit(load_missile, (350, 100))
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                            explosion = pygame.transform.scale(explosion, (10*missile, 10*missile))
                            screen.blit(explosion, (377, 100))
                        elif boom_num < 9:
                            explosion = pygame.transform.scale(explosion, (10*missile, 10*missile))
                            screen.blit(explosion, (377, 100))
                    elif missile < 21:
                        if boom_num < 3:
                            screen.blit(load_missile, (350, 100))
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                            explosion = pygame.transform.scale(explosion, (15*missile, 15*missile))
                            screen.blit(explosion, (323, 35))
                        elif boom_num < 9:
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                            explosion = pygame.transform.scale(explosion, (15*missile, 15*missile))
                            screen.blit(explosion, (323, 35))
                    elif missile < 23:
                        if boom_num < 3:
                            screen.blit(load_missile, (350, 100))
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                            explosion = pygame.transform.scale(explosion, (15*missile, 15*missile))
                            screen.blit(explosion, (300, 35))
                        elif boom_num < 9:
                            explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_num)+'.png')
                            explosion = pygame.transform.scale(explosion, (15*missile, 15*missile))
                            screen.blit(explosion, (300, 35))
                    if count == 3:          #moving on the animation
                            count = 0
                            boom_num += 1
                    blit_all()
                    victory_banner = pygame.image.load('Data/sprites/VICTORY.png')
                    screen.blit(victory_banner, (75, 300))
                    if boom_num == 8:
                            var.CockpitRun = False
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
                            position_boom[num] = (random.randint(0, 900), random.randint(0, 700))
                            size_boom[num]=(random.randint(75, 300))
                    count_boom[num] += 1
                #blitting the large explosion
                lrg_explosion = pygame.image.load('Data/sprites/explosion/'+str(boom_tick)+'.png')
                lrg_explosion = pygame.transform.scale(lrg_explosion, (600, 600))
                screen.blit(lrg_explosion, (160, -30))
                if count == 5:              #ticking the large explosion
                    boom_tick += 1
                    count = 0
                if boom_tick == 7:          #ends the game after a cetain amount of time
                    exit()
                count += 1
                faliure_banner = pygame.image.load('Data/sprites/FAILED.png')
                screen.blit(faliure_banner, (135, 50))

            pygame.display.update()
            fps.tick(60)
