import pygame;
from pygame.sprite import Sprite;
from turret import Turret;
import time

#creates a turret bot
class TurretBot(Turret):
	def __init__(self, screen, square, game_settings):
		
		#sets turret's health and speed
		self.shoot_speed = 1.5;
		self.health = 5;
		self.image = pygame.image.load('images/shooter_idle.png');
		self.image = pygame.transform.scale(self.image, (105,105));
		self.screen = screen;
		self.square = square;
		self.name = "turretbot";
		self.can_shoot = True;
		self.can_make_battery = False;		
		super(TurretBot, self).__init__();
		
	#changes images depending on if turret is firing
	def change_image(self, should_shoot):
		if should_shoot:
			self.image = pygame.image.load('images/shooter_attack.png');
			self.image = pygame.transform.scale(self.image, (105,105));
		else:		
			self.image = pygame.image.load('images/shooter_idle.png');
			self.image = pygame.transform.scale(self.image, (105,105));