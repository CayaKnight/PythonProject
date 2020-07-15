import pygame
import pygame_menu
import sys
from settings import Settings
from square import Square
from background import Background
import game_functions as gf
from pygame.sprite import Group, groupcollide
from robot import Robot
from turret_icon import Turret_Icon
import time
from generator import Generator
import game
import statmenu

#creates start menu
def startmenu():
    font = pygame_menu.font.FONT_MUNRO
    myimage = pygame.image.load('images/menu_background.png')
    background_image = pygame_menu.baseimage.BaseImage(
        image_path='images/menu_background.png',
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
    mytheme = pygame_menu.themes.Theme(background_color=background_image,
                                       title_shadow=True,
                                       title_background_color=(255, 255, 255),
                                       title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                                       title_font=font,
                                       title_font_size=112,
                                       title_offset=(225,80),
                                       widget_font=font,
                                       widget_font_size=70,
                                       widget_shadow=True)             
    menu = pygame_menu.Menu(756, 1152, 'Chrome Vs. Rust',theme=mytheme)

    #starts gameplay
    menu.add_button('Play', game.create)

    #lead to synosips of game
    menu.add_button('About', about)
    #switches to stat menu
    menu.add_button('Stats', statmenu.stats)

    #exits game
    menu.add_button('Quit', pygame_menu.events.EXIT)
    surface = pygame.display.get_surface()
    menu.mainloop(surface)
def about():
    font =pygame_menu.font.FONT_OPEN_SANS_ITALIC
    story = "Need something to clean up around the house? Get back at whoever stole your parking spot? Or just a way to get rid of pests? Meet CAMBOT’s new line of TurretBots. Their soup can shape makes them easy to store and adorable to look at. Each TurretBot is made entirely from the highest quality chrome available and decorated with LED lights.  CAMBOT’s research team has devoted years of their lives to produce a variety of TurretBots with different functions to suit your needs. TurretBot, your favorite chrome companion"
    disclaimer = "TurretBot are product of CAMBOT INC. Do not attempt to duplicate or take apart your Turretbot.\n"\
                 "Do not purchase a TurretBot if you are pregnant or planning on becoming pregnant.\n"\
                 "Children \n\n\n\n\n under age 5 should not be with TurretBot unsupervised. "\
                 "Prolonged contact with TurretBots may include, but are not limited to: "\
                 "Nausea and vomiting, Diarrhea, Headache, Fever, Dizziness and disorientation, Weakness and fatigue, Hair loss, Infections and,  Low blood pressure. CAMBOT INC. is not responsible for any sickness resulting from TurretBot."
    display_info = pygame.display.Info()
    gamedisplay=game.screen
    gamedisplay.fill((0,0,0))

    mytheme = pygame_menu.themes.Theme(background_color=(0, 0, 0),
									   title_shadow=True,
									   title_background_color=(0, 0, 0, 0),
									   title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
									   title_font=font,
									   title_font_size=60,
									   widget_font=font,
                                                                           widget_margin=(-20,0),
                                                                           widget_offset=(0,0),
                                                                           widget_alignment=pygame_menu.locals.ALIGN_LEFT,
									   widget_font_size=45,
									   widget_shadow=False)
    menu = pygame_menu.Menu(556,1052, 'About The TurretBot',theme=mytheme,menu_position=(50,50),column_force_fit_text=False)
    menu.add_label(story, max_char=-1, font_size=18,font_color=(255,255,255))
    menu.add_vertical_margin(100)
    menu.add_label(disclaimer, max_char=-1, font_size=12,font_color=(255,255,255))
    menu.add_button('Back', startmenu)
    surface = pygame.display.get_surface()
    menu.mainloop(surface)
startmenu()
