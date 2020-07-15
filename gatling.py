import pygame;
from pygame.sprite import Sprite;
from turret import Turret;

#creates a gatling turret
class Gatling(Turret):
	def __init__(self, screen, square,game_settings):
		self.shoot_speed = .2;
		self.health = 6;
		self.image = pygame.image.load('images/gatling_idle.png');
		self.image = pygame.transform.scale(self.image, (105,105));
		self.screen = screen;
		self.square = square;
		self.name = "gatling";
		self.can_shoot = True;
		self.can_make_battery = False;
		super(Gatling, self).__init__();
		
	#changes images depending on if turret is firing
	def change_image(self, should_shoot):
		if should_shoot:
			self.image = pygame.image.load('images/gatling_attack.png');
			self.image = pygame.transform.scale(self.image, (105,105));
		else:		
			self.image = pygame.image.load('images/gatling_idle.png');
			self.image = pygame.transform.scale(self.image, (105,105));