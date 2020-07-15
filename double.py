import pygame;
from pygame.sprite import Sprite;
from turret import Turret;

#create a double turrett
class Double(Turret):
	def __init__(self, screen, square,game_settings):
		self.shoot_speed = .5;
		self.health = 15;
		self.image = pygame.image.load('images/double_idle.png');
		self.image = pygame.transform.scale(self.image, (105,105));
		self.screen = screen;
		self.square = square;
		self.name = "double";
		self.can_shoot = True;
		self.can_make_battery = False;
		super(Double, self).__init__();
	#changes images depending on if turret is firing
	def change_image(self, should_shoot):
		if should_shoot:
			self.image = pygame.image.load('images/double_attack.png');
			self.image = pygame.transform.scale(self.image, (105,105));
		else:		
			self.image = pygame.image.load('images/double_idle.png');
			self.image = pygame.transform.scale(self.image, (105,105));