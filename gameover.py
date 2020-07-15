import pygame;
import pygame_menu
from settings import Settings;
from square import Square;
from background import Background;
import game_functions as gf;
from pygame.sprite import Group, groupcollide
from robot import Robot;
from turret_icon import Turret_Icon;
import time
from generator import Generator
import game
import statmenu

#creates a game over menu
def GameOver():
    GOfont=pygame_menu.font.FONT_FRANCHISE
    GOimage = pygame.image.load('images/gameover.png')
    background_image = pygame_menu.baseimage.BaseImage(
        image_path='images/gameover.png',
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
    GOtheme = pygame_menu.themes.Theme(background_color=background_image,
                                       title_shadow=True,
                                       title_background_color=(255, 255, 255),
                                       title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                                       title_font=GOfont,
                                       title_font_size=112,
                                       title_offset=(400,80),
                                       widget_font=GOfont,
                                       widget_font_size=72,
                                       widget_shadow=True)
    menu = pygame_menu.Menu(756, 1152, 'GAME OVER!',theme=GOtheme)
	
	#switches to stat menu
    menu.add_button('Stats', statmenu.stats)
	
	#exits game
    menu.add_button('Quit', pygame_menu.events.EXIT)
    surface = pygame.display.get_surface()
    menu.mainloop(surface)