import pygame;
import pygame_menu
from settings import Settings;
import game
import sys
import game_functions as gf;
def stats():
	display_info = pygame.display.Info()
	gamedisplay=game.screen
	gamedisplay.fill((0,0,0))

	font = pygame_menu.font.FONT_MUNRO
	
	#creates a menu that displays the player's stats (I really like menues now)
	mytheme = pygame_menu.themes.Theme(background_color=(0, 0, 0), # transparent background
									   title_shadow=True,
									   title_background_color=(0, 0, 0, 0),
									   title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
									   title_font=font,
									   title_font_size=60,
									   title_offset = (550,100),
									   widget_font=font,
									   widget_offset = (30,0),
									   widget_font_size=50,
									   widget_shadow=False,
									   widget_alignment=pygame_menu.locals.ALIGN_LEFT)			   
	menu = pygame_menu.Menu(756, 1152, 'Stats',theme=mytheme,menu_position=(0,0))
	menu.add_button('Back', pygame_menu.events.RESET, align=pygame_menu.locals.ALIGN_LEFT)
	menu.add_button('Quit', pygame_menu.events.EXIT,align=pygame_menu.locals.ALIGN_LEFT)
	menu.add_label("Kills: "+str(game.game_settings.robots_killed), margin=(250,0),font_color=(255,255,255))
	menu.add_label("Boss Kills: "+str(game.game_settings.bosses_killed), margin=(250,0),font_color=(255,255,255))
	menu.add_label("Total Battery Used: "+str(game.game_settings.battery_used), margin=(250,0),font_color=(255,255,255))
	menu.add_label("DoubleBots Made: "+str(game.game_settings.doubles_made), margin=(250,0),font_color=(255,255,255))
	menu.add_label("GatlingBots Made: "+str(game.game_settings.gatling_made), margin=(250,0),font_color=(255,255,255))
	menu.add_label("ToxixBots Made: "+str(game.game_settings.toxic_made), margin=(250,0),font_color=(255,255,255))
	menu.add_label("Turrets Lost: "+str(game.game_settings.turrets_lost), margin=(250,0),font_color=(255,255,255))
	menu.add_label("Waves Survived: "+str(game.game_settings.wave_num),margin=(250,0),font_color=(255,255,255))
	surface = pygame.display.get_surface()
	menu.mainloop(surface)