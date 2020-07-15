import sys
import pygame
from shooter import TurretBot
from gatling import Gatling
from bullet import Bullet
from generator import Generator
from robot import Robot
from double import Double
from toxic import Toxic
import time


#removes turret from square when upgrade or when destroyed
def remove_turret_in_square(square, turrets):
    for turret in turrets:
        if turret.square == square:
            turrets.remove(turret)
game_log = ''

#checks for event such as collision, movement, turret purchases, etc.
def check_events(screen, game_settings,squares,turrets,bullets,icons,tick):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if game_settings.game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                for square in squares:
                    if square.rect.collidepoint(mouse_x,mouse_y):
                        if(game_settings.chosen_turret == 2 and game_settings.total_battery >= 50):
                            #if player attempts to downgrade a turret to previous level, note is written in game log
                            for turret in turrets:
                                if turret.square == square and (turret.name=='gatling' or turret.name=='double' or turret.name=='turretbot'):
                                    game_log = 'You can\'t downgrade your hero'
                                else:
                                    turrets.add(TurretBot(screen,square,game_settings))                          
                            remove_turret_in_square(square, turrets)
                            turrets.add(TurretBot(screen,square,game_settings))
                            game_settings.total_battery -= 50
                            game_settings.battery_used +=50
                            game_settings.shooters_made+=1


                        elif(game_settings.chosen_turret == 3 and game_settings.total_battery >= 200):
                            for turret in turrets:
                                if turret.square == square:
                                
                                #removes image of turretbot
                                #creates double turret
                                    if turret.name=='turretbot':
                                        turrets.remove(turret)
                                        turrets.add(Double(screen,square,game_settings))
                                        game_settings.total_battery -= 200
                                        game_settings.battery_used +=200
                                        game_settings.doubles_made+=1

                        elif(game_settings.chosen_turret == 4 and game_settings.total_battery >= 500):
                            for turret in turrets:
                                if turret.square == square:
                                
                                #removes image of double turret
                                #creates gatling turret
                                    if turret.name=='double':
                                        turrets.remove(turret)
                                        turrets.add(Gatling(screen,square,game_settings))
                                        game_settings.total_battery -= 500  
                                        game_settings.battery_used +=500
                                        game_settings.gatling_made+=1
                                        
                        elif(game_settings.chosen_turret == 5 and game_settings.total_battery >= 750):
                            for turret in turrets:
                                if turret.square == square:
                                
                                #removes image of gatling turret
                                #creates toxic turret
                                    if turret.name=='gatling':
                                        turrets.remove(turret)
                                        turrets.add(Toxic(screen,square,game_settings))
                                        game_settings.total_battery -= 750  
                                        game_settings.battery_used +=750
                                        game_settings.toxic_made+=1   
                        
                        #if player buys a generator, cost is subtracted from battery                        
                        elif(game_settings.chosen_turret == 1 and game_settings.total_battery >= 50):
                            remove_turret_in_square(square, turrets)
                            turrets.add(Generator(screen,square,game_settings)) 
                            game_settings.total_battery -= 50
                            game_settings.battery_used +=50
                
                #check if player has made a selection in the hotbar
                for icon in icons:
                    if icon.rect.collidepoint(mouse_x,mouse_y):
                        game_settings.chosen_turret = icon.slot
                        icon.chosen = True
                    else:
                        icon.chosen = False   
            #determines if square should be highlighted
            elif event.type == pygame.MOUSEMOTION:
                for square in squares:
                    if square.rect.collidepoint(event.pos):
                        game_settings.highlighted_square = square
def update_screen(screen,game_settings,background,robots,squares,turrets,bullets,tick,icons,wave_num):
    screen.blit(background.image, background.rect)
    all_clear = False
    #draws a blue rectangle around the turret currently selected
    for icon in icons:
        screen.blit(icon.image, icon.rect)
        if icon.slot == game_settings.chosen_turret:
            pygame.draw.rect(screen, (180,180,255), (icon.rect.left -10, icon.rect.top-10,int(90),int(100)),2)
            s = pygame.Surface((int(90),int(100)), pygame.SRCALPHA)   # per-pixel alpha
            s.fill((0,0,200,35))                        
            screen.blit(s, (icon.rect.left-10, icon.rect.top-10))

    #highlights the square that the mouse is hovering over
    if game_settings.highlighted_square != 0:
        pygame.draw.rect(screen, (255,215,255), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares['square_width'],game_settings.squares['square_height']),2)
        s = pygame.Surface((game_settings.squares['square_width'],game_settings.squares['square_height']), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((255,215,255,35))                        
        screen.blit(s, (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top))
    #creates turrets
    for turret in turrets:
        turret.draw_me()
        if turret.name == 'generator':
            turret.draw_me()
        #allows turrets to fire
        should_shoot = time.time() - turret.last_shot > turret.shoot_speed
        
        in_my_row = game_settings.robot_in_row[turret.factory_row] > 0
        #give the toxic turret a bullet spray mechanic
        if turret.name == 'toxic':
            in_my_row = True
        #checks if turret and robot are in the same row
        #if turret can shoot and theres a robot in the row,it will shoot
        turret.change_image(in_my_row and should_shoot)
        can_shoot = turret.can_shoot
        
        #checks which turrets on the screen can make batteries
        can_make_battery = turret.can_make_battery
        
        #determines when the last batteries were spawned
        should_make_battery = (time.time() - turret.last_battery) > turret.battery_speed
        
        #draws bullets if previous conditions are met
        if should_shoot and in_my_row and can_shoot:
            bullets.add(Bullet(screen,turret,tick))
            turret.last_shot = time.time()

        #if it has been long enough and there a generator on the field,
        #make some batteries
        if can_make_battery and should_make_battery:
            turret.make_battery(game_settings)
            turret.last_battery = time.time()
    
    #robots 'walk' across the screen
    for robot in robots.sprites():
        if game_settings.game_active:
            robot.update_me()
        robot.draw_me()
        
        #if robot makes it to the end of the screen, the player loses
        if robot.rect.left <= robot.screen_rect.left:
            game_settings.game_lost= True

    #creates instaces of bullets as needed
    for bullet in bullets.sprites():    
        bullet.update_me()
        bullet.draw_me()
    #displays and updates the current wave
    wave_font=pygame.font.SysFont("Consolas",36)
    waveText=wave_font.render("WAVE " + str(wave_num),1,(255,0,0))
    screen.blit(waveText,(245,70))
    
    #displays and updates the player's score
    score_font = pygame.font.SysFont("Consolas",24)
    battery_render = score_font.render("Score: " + str((tick*2)),1,(0,0,0))
    screen.blit(battery_render,(20,30))

    #displays and updates the number of robot kills
    score_render = score_font.render("Kills: "+str(game_settings.robots_killed),1,(0,0,0))
    screen.blit(score_render,(20,60))
    
    #displays and updates the number of boss robot kills
    score_render = score_font.render("Boss Kills: "+str(game_settings.bosses_killed),1,(0,0,0))
    screen.blit(score_render,(20,90))
    
    ##displays and updates the amount of batteries the player has to spend
    battery_render = score_font.render("Battery: "+str(game_settings.total_battery),1,(0,0,0))
    screen.blit(battery_render,(20,120))
    
    #displays the prices of each turret 
    cost_font = pygame.font.SysFont("Arial",20)
    battery_render = cost_font.render("50              50              200             500             750         ",1,(0,0,0))
    screen.blit(battery_render,(490,130))

    battery_render = cost_font.render("                                               upgrade  >   upgrade  >   upgrade",1,(0,0,0))
    screen.blit(battery_render,(400,15))